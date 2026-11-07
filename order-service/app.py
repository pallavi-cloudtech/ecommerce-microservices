from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def create_order():

    response = requests.get(
        "http://cart-service:5002/cart",
        timeout=5
    )

    cart = response.json()

    if not cart:
        return jsonify({"message": "Cart is empty"}), 400

    order = {
        "order_id": 101,
        "items": cart,
        "status": "Order placed successfully"
    }

    return jsonify(order), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)