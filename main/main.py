"""Main app of the microservice
"""
from dataclasses import dataclass

from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint

import requests

from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id: int
    user_id: int
    product_id: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route("/api/products")
def index():
    """Returns all Products, synced with flask's db and django's dbs
    """
    return jsonify(Product.query.all())


@app.route("/api/products/<int:id>/like", methods=["POST"])
def like(id):
    """Adds a like for a products, made by a user.
    """
    req = requests.get("http://127.0.0.1:8000/api/users")
    json_req = req.json()

    try:
        # adding Product-User details in ProductUser flask's table
        productUser = ProductUser(user_id=json_req['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()

        publish(method="product_liked", body=id)

    except:
        abort(400, "You already liked this product")

    return jsonify({"message": "success"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
