"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, FavoriteCharacter, FavoritePlanet
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@app.route('/user', methods=['GET'])
def list_user():
    user = User.query.all()
    data =[user.serialize() for user in users]

    return jsonify(data), 200

@app.route('/character', methods=['GET'])
def list_character():
    character = Character.query.all()
    data =[character.serialize() for character in characters]

    return jsonify(data), 200