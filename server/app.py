#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from sqlalchemy import desc, asc

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>My Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    # return 'get all bakeries'
    return jsonify([b.to_dict() for b in Bakery.query.all()])

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    # return all goods by bekery id
    return jsonify(Bakery.query.get(id).to_dict())

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    # return 'get all baked goods by price' 
    # sorts the baked goods by price in descending order
    return jsonify([bg.to_dict() for bg in BakedGood.query.order_by(BakedGood.price.desc()).all()])
   

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    # return 'get the most expensive baked good'
    return jsonify(BakedGood.query.order_by(BakedGood.price.desc()).first().to_dict())

if __name__ == '__main__':
    app.run(port=5555, debug=True)
