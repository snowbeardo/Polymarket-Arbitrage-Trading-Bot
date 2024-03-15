from flask import Flask, jsonify
import json
app = Flask(__name__)

#To load products data

def load_products_data():
    with open('products.json','r',encoding="utf-8")as file:
        return json.load(file)

@app.route('/',methods=['GET'])
def hello():
    return "hello"

#To load products page
@app.route('/products',methods=['GET'])
def get_products():
    data = load_products_data()
    return jsonify(data)

@app.route('/products/<int:product_id>',methods=['GET'])
def get_product_by_id(product_id):
    products = load_products_data()
    product = None

    for p in products:
        if p["id"] == product_id:
            product = p
            break
    return jsonify(product) if product else ('Product Not Found', 404)

app.run(debug=True)