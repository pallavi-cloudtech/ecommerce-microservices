from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 20000},
    {"id": 3, "name": "Headphones", "price": 2000}
]

@app.route('/products')
def get_products():
    return jsonify(products)

@app.route('/')
def home():
    return "Welcome to Product Service!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)