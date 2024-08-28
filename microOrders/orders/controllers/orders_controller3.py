import requests
from flask import Blueprint, request, jsonify, session
from orders.models.orders_model import Orders
from db.db import db

orders_controller = Blueprint('orders_controller', __name__)

@orders_controller.route('/api/orders', methods=['GET'])
def get_orders():
    print("listado de ordenes")
    orders = Orders.query.all()
    result = [{'id':order.id, 'userName': order.userName,
        'userEmail': order.userEmail,
        'saletotal': str(order.saletotal),
        'date': order.date} for order in orders]
    return jsonify(result)

# Get single user by id
@orders_controller.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    print("obteniendo orden")
    order = Orders.query.get_or_404(order_id)
    return jsonify({'id':order.id,
        'userName': order.userName,
        'userEmail': order.userEmail,
        'saletotal': str(order.saletotal),
        'date': order.date})

@orders_controller.route('/api/orders', methods=['POST'])
def create_orders():
    print("creando orden")
    data = request.get_json()

    user_name = data.get('username')
    user_email = data.get('email')
    
    if not user_name or not user_email:
        user_name = session.get('username')
        user_email = session.get('email')
    
    products = data.get('products')


    sale_total = 0
    product_updates = []

    for product in products:
        product_id = product.get('id')
        quantity = product.get('quantity')

        product_response = requests.get(f'http://192.168.80.3:5003/api/products/{product_id}')
        db_product = product_response.json()

        sale_total += float(db_product['price']) * quantity
        product_updates.append({'id': product_id, 'quantity': db_product['quantity'] - quantity})

    update_response = requests.put(
        'http://microProducts:5003/api/products/update_quantity',
        json=product_updates
    )

    #saletotal= orderData.get('saletotal')
   # product = Products.query.get(product_id)
   # product_total = product.price * quantity
    #print(products_info,quantity)
    #new_user = Users(name="oscar", email="oscar@gmail", username="omondragon", password="123")
   # saletotal=0.0
    #saletotal += product.price * 2
    new_order = Orders(userName=user_name, userEmail=user_email, saleTotal=sale_total)
           # ,saletotal = orderData.get('saletotal')
                #,saleTotal=0)
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201
