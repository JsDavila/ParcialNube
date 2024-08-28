
from flask import Blueprint, request, jsonify, session
from orders.models.orders_model import Orders  # Asegúrate de que el modelo Order está correctamente importado
from db.db import db  # Asegúrate de que la base de datos esté correctamente importada
from microProducts.products.models.products_model import Products  # Asegúrate de que el modelo Product está correctamente importado

order_controller = Blueprint('order_controller', __name__)

@orders_controller.route('/api/orders', methods=['GET'])
def get_all_orders():
    orders = Orders.query.all()
    return jsonify([order.to_dict() for order in orders]), 200

@orders_controller.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Orders.query.get(order_id)
    if order is None:
        return jsonify({'message': 'Orden no encontrada'}), 404
    return jsonify(order.to_dict()), 200

@order_controller.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    user_name = session.get('username')
    user_email = session.get('email')

    if not user_name or not user_email:
        return jsonify({'message': 'Información de usuario inválida'}), 400

    products = data.get('products')
    if not products or not isinstance(products, list):
        return jsonify({'message': 'Falta o es inválida la información de los productos'}), 400

    # Calcular el total de la venta
    total = 0
    for item in products:
        product = Product.query.get(item['product_id'])
        if product is None or product.stock < item['quantity']:
            return jsonify({'message': f'Producto con ID {item["product_id"]} no disponible o cantidad insuficiente'}), 400
        total += product.price * item['quantity']

    # Actualizar el inventario
    for item in products:
        product = Product.query.get(item['product_id'])
        product.stock -= item['quantity']
        db.session.commit()

    # Crear una nueva instancia de Order y guardarla en la base de datos
    new_order = Order(user_name=user_name, user_email=user_email, total=total, products=products)
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Orden creada exitosamente', 'order_id': new_order.id}), 201

