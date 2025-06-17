from flask import Blueprint, request, jsonify
from ..models.restaurant import Restaurant
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..app import db

restaurant_bp = Blueprint("restaurant_bp", __name__, url_prefix="/restaurants")

@restaurant_bp.route("", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants]), 200

@restaurant_bp.route("/<int:id>", methods=["GET"])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    pizzas = [rp.pizza.to_dict() for rp in restaurant.restaurant_pizzas]
    data = restaurant.to_dict()
    data["pizzas"] = pizzas
    return jsonify(data), 200

@restaurant_bp.route("/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return "", 204
