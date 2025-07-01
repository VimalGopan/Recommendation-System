from flask import Flask, jsonify, render_template, request
from model import RecommenderSystem

app = Flask(__name__)
model = RecommenderSystem("Beauty.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random-products")
def random_products():
    # Return a list of objects: {id, name}
    product_ids = model.get_random_products(n=12)
    products = [{"id": pid, "name": model.get_product_name(pid)} for pid in product_ids]
    return jsonify({"products": products})

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    product_id = data.get("product_id")
    product_name = model.get_product_name(product_id)
    recommendations = model.get_recommendations(product_id)  # returns list of (id, name)
    result = {
        "product_id": product_id,
        "product_name": product_name,
        "recommendations": [{"id": rid, "name": rname} for rid, rname in recommendations]
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
