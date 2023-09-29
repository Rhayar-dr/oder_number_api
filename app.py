from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {
        "order_number": 1,
        "product_id": 101,
        "product_name": "Laptop",
        "email_customer": "john@example.com",
        "shipping_status": "Shipped"
    },
    {
        "order_number": 2,
        "product_id": 102,
        "product_name": "Macbook",
        "email_customer": "lola@example.com",
        "shipping_status": "Arrived"
    },
    {
        "order_number": 3,
        "product_id": 103,
        "product_name": "Iphone",
        "email_customer": "bruna@example.com",
        "shipping_status": "Arrived"
    },
    {
        "order_number": 4,
        "product_id": 104,
        "product_name": "Mug",
        "email_customer": "pop@example.com",
        "shipping_status": "Ordered"
    }
]

@app.route('/api/orders/<int:order_number>', methods=['GET'])
def get_order(order_number):
    order = next((item for item in data if item["order_number"] == order_number), None)
    if order:
        return jsonify(order), 200
    else:
        return jsonify({"message": "Order not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
