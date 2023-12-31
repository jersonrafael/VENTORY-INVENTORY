from flask import render_template
from app import app

from bson import ObjectId
from conn import categorys,products

#SEE THE CATEGORYS
@app.route('/category/<category_id>')
def catSearch(category_id):
    product_quantity = products.count_documents({"cat_id": category_id})
    print(product_quantity)
    find_cat = categorys.find_one({"_id":ObjectId(category_id)})
    all_products_cat = products.find({"cat_id": category_id})
    return render_template('categorys.html', name=find_cat,products_find=all_products_cat, product_quantity=product_quantity)

#SEE ALL CATEGORYS
@app.route('/categorias')
def categorias():
    getCategorys = categorys.find()

    return render_template('seccionCategorias.html', allcategorys=getCategorys)