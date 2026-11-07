from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

cart = []
@app.route('/cart', methods=['POST'])
def add_to_cart():

    data = request.get_json()

    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    response = requests.get(
        "http://product-service:5001/products",
        timeout=5
    )

    products = response.json()

    product = next(
        (p for p in products if p['id'] == product_id),
        None
    )

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    item = {
        "id": product['id'],
        "name": product['name'],
        "price": product['price'],
        "quantity": quantity
    }

    cart.append(item)

    return jsonify({
        "message": "Product added successfully!",
        "cart": cart
    }), 201


@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify(cart), 200
    
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)
    