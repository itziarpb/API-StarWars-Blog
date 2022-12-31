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

@api.route('/character/<int:character_id>', methods=['GET'])
def one_character(character_id):
    character = Character.query.filter(Character.id == character_id).first()

    return jsonify(character.serialize()), 200

@api.route('/planet', methods=['GET'])
def list_planets():
    planets = Planet.query.all()
    data =[planet.serialize() for planet in planets]

    return jsonify(data), 200

@api.route('/planet/<int:planet_id>', methods=['GET'])
def one_planet(planet_id):
    planet = Planet.query.filter(Planet.id == planet_id).first()

    return jsonify(planet.serialize()), 200

@api.route('/user/<int:idUser>/favorites', methods=['GET'])
def list_favorites(idUser):
    usercharacters = FavoriteCharacter.query.filter(FavoriteCharacter.user_id == idUser)
    datacharacters =[usercharacter.serialize() for usercharacter in usercharacters]
    userplanets = FavoritePlanet.query.filter(FavoritePlanet.user_id == idUser)
    dataplanets =[userplanet.serialize() for userplanet in userplanets]
    
    return jsonify(datacharacters, dataplanets ), 200