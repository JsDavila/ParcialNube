from flask import Blueprint, request, jsonify
from products.models.products_model import Products
from db.db import db

products_controller = Blueprint('products_controller', __name__)

@products_controller.route('/api/products', methods=['GET'])
def get_products():
    print("listado de productos")
    products = Products.query.all()
    result = [{'id':product.id, 'name': product.name, 'price': product.price, 'quantity': product.quantity} for product in products]
    return jsonify(result)

# Get single user by id
@products_controller.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    print("obteniendo producto")
    product = Products.query.get_or_404(product_id)
    return jsonify({'id':product.id, 'name': product.name, 'price': product.price, 'quantity': product.quantity})

@products_controller.route('/api/products', methods=['POST'])
def create_products():
    print("creando producto")
    data = request.json
    #new_user = Users(name="oscar", email="oscar@gmail", username="omondragon", password="123")
    new_product = Products(name=data['name'], price=data['price'], quantity=data['quantity'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

# Update an existing user
@products_controller.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    print("actualizando producto")
    user = Products.query.get_or_404(product_id)
    data = request.json
    user.name = data['name']
    user.price = data['price']
    user.quantity = data['quantity']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

# Delete an existing user
@products_controller.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Products.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})
@products_controller.route('/api/products/update_quantity', methods=['PUT'])
def update_product_quantity():
    print("actualizando cantidades de productos")
    data = request.json

    if not isinstance(data, list):
        return jsonify({'message': 'Se espera una lista de productos para actualizar'}), 400

    for product_update in data:
        product_id = product_update.get('id')
        new_quantity = product_update.get('quantity')

        if product_id is None or new_quantity is None:
            return jsonify({'message': 'Cada producto debe tener un id y una cantidad'}), 400

        product = Products.query.get_or_404(product_id)
        product.quantity = new_quantity
        db.session.commit()

    return jsonify({'message': 'Cantidades de productos actualizadas exitosamente'})

