"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, FavoriteCharacter, FavoritePlanet
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/user', methods=['GET'])
def list_users():
    users = User.query.all()
    data =[user.serialize() for user in users]

    return jsonify(data), 200

@api.route('/character', methods=['GET'])
def list_characters():
    characters = Character.query.all()
    data =[character.serialize() for character in characters]

    return jsonify(data), 200

@api.route('/planet', methods=['GET'])
def list_planets():
    planets = Planet.query.all()
    data =[planet.serialize() for planet in planets]

    return jsonify(data), 200

@api.route('/favoriteCharacter', methods=['GET'])
def list_favorites_characters():
    favorite_characters = FavoriteCharacter.query.all()
    data =[favorite_character.serialize() for favorite_character in favorite_characters]

    return jsonify(data), 200

@api.route('/favoritePlanet', methods=['GET'])
def list_favorites_planets():
    favorites_planets = FavoritePlanet.query.all()
    data =[favorites_planet.serialize() for favorites_planet in favorites_planets]

    return jsonify(data), 200

@api.route('/user/<idUser>/favorites', methods=['GET'])
def list_favorites(idUser):
    usercharacters = FavoriteCharacter.query.filter(FavoriteCharacter.user_id == idUser)
    datacharacters =[usercharacters.serialize() for usercharacter in usercharacters]
    
    return jsonify(datacharacters), 200