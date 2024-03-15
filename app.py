from flask import Flask, jsonify, request
import json
app = Flask(__name__)

#To load products data

def load_products_data():
    with open('products.json','r',encoding="utf-8")as file:
        return json.load(file)
    
#To save data
    
def save_products_data(products):
    with open('products.json','w')as file:
        json.dump(products,file,indent=4)

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

@app.route('/products',methods=['POST'])
def create_product():
    new_product = request.json
    products = load_products_data()
    products.append(new_product)
    save_products_data(products)
    return new_product

@app.route('/products/<int:product_id>',methods=['PUT'])
def update_product(product_id):
    products = load_products_data()
    product = None

    for p in products:
        if p["id"] == product_id:
            product = p
            break

    updated_product = request.json #Data recieved from front end
    product.update(updated_product)
    save_products_data(products)
    return updated_product

@app.route('/products/<int:product_id>',methods=['DELETE'])
def delete_product(product_id):
    products = load_products_data()
    
    updated_list =list(filter(lambda p: p["id"] != product_id,products))
    save_products_data(updated_list)
    return 'Deleted Successfully', 204

app.run(debug=True)