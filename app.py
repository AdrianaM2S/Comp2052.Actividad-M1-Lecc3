from flask import Flask, request, jsonify

app = Flask(__name__)

# List of temporary storage for users and products
users = []
products = []

# Route to GET /info
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "message": "Product and user management system."
    })

# Route to POST /create_user
@app.route("/create_user", methods=["POST"])
def create_user():
    data = request.json
    # Data validation
    name = data.get("name")
    email = data.get("email")
    Id = data.get("Id")

    if not name or not email:
        return jsonify({
            "error": "Required fields are missing. Must include 'name' and 'email'."
        }), 400

    user = {"Id": Id, "name": name, "email": email}
    users.append(user)
    return jsonify({
        "message": "User created", "users": users
        })

# Route to GET /users
@app.route("/users", methods=["GET"])
def list_users():
    return jsonify({
        "users": users
    })

# Route to POST /create_product
@app.route("/create_product", methods=["POST"])
def create_product():
    data = request.json
    productId = data.get("productId")
    name = data.get("name")
    price = data.get("price")
    available = data.get("available", True)

    if not name or not price:
        return jsonify({
            "error": "Name and price are required"
            }), 400

    product = {"productId": productId, "name": name, "price": price, "available": available}
    products.append(product)
    return jsonify({
        "message": "Product created", "product": product
        })

# Route to GET /products
@app.route("/products", methods=["GET"])
def list_products():
    return jsonify({"products": products})

if __name__ == "__main__":
    app.run(debug=True)
