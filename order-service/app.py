from flask import Flask, jsonify
import requests

app = Flask(__name__)

orders = []

CART_SERVICE_URL = "http://127.0.0.1:5002/cart"


@app.route('/')
def home():
    return "Welcome to Order Service!"


@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)


@app.route('/orders', methods=['POST'])
def create_order():

    try:
        response = requests.get(CART_SERVICE_URL, timeout=5)
        response.raise_for_status()
        cart = response.json()

        if not cart:
            return jsonify({"error": "Cart is empty"}), 400

        total = sum(
            item['price'] * item['quantity']
            for item in cart
        )

        order = {
            "order_id": len(orders) + 1,
            "items": cart,
            "total_price": total,
            "status": "Order Confirmed"
        }

        orders.append(order)

        return jsonify(order), 201

    except requests.RequestException:
        return jsonify({"error": "Cart Service is unavailable"}), 503


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)