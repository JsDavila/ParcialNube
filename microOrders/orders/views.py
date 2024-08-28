from flask import Flask, jsonify
from orders.controllers.orders_controller import orders_controller
from db.db import db
from flask_cors import CORS

app = Flask(__name__)
#CORS(app)
app.secret_key = 'secret123'
app.config.from_object('config.Config')
db.init_app(app)

# Registrando el blueprint del controlador de usuarios
app.register_blueprint(orders_controller)
CORS(app, supports_credentials=True)

if __name__ == '__main__':
    #with app.app_context():
     # db.create_all()	
    app.run(host='0.0.0.0', port=5004)
