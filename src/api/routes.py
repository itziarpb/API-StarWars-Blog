"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, FavoriteCharacter, FavoritePlanet
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/character', methods=['GET'])
def list_characters():
    characters = Character.query.all()
    data =[character.serialize() for character in characters]

    return jsonify(data), 200

@api.route('/character/<int:character_id>', methods=['GET'])
def one_character(character_id):
    character = Character.query.filter_by(id = character_id).first()

    if character:
        return jsonify(character.serialize()), 200
    
    return jsonify ({"mensaje": "Personaje no encontrado"}), 400

@api.route('/planet', methods=['GET'])
def list_planets():
    planets = Planet.query.all()
    data =[planet.serialize() for planet in planets]

    return jsonify(data), 200

@api.route('/planet/<int:planet_id>', methods=['GET'])
def one_planet(planet_id):
    planet = Planet.query.filter_by(id = planet_id).first()

    if planet:
        return jsonify(planet.serialize()), 200
    
    return jsonify ({"mensaje": "Planeta no encontrado"}), 400

@api.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    data =[user.serialize() for user in users]

    return jsonify(data), 200

@api.route('/users/<int:idUser>/favorites', methods=['GET'])
def list_favorites(idUser):
    usercharacters = FavoriteCharacter.query.filter(FavoriteCharacter.user_id == idUser)
    datacharacters =[usercharacter.serialize() for usercharacter in usercharacters]
    userplanets = FavoritePlanet.query.filter(FavoritePlanet.user_id == idUser)
    dataplanets =[userplanet.serialize() for userplanet in userplanets]
    data = datacharacters + dataplanets
    
    return jsonify(data ), 200

@api.route('<int:idUser>/favorite/character/<int:idCharacter>', methods=['POST'])
def new_character(idUser,idCharacter):
    data = request.json
    me = FavoriteCharacter(user_id=idUser, character_id=idCharacter)
    db.session.add(me)
    db.session.commit()

    return jsonify({"mensaje": "Personaje añadido a favoritos"})

@api.route('<int:idUser>/favorite/planet/<int:idPlanet>', methods=['POST'])
def new_planet(idUser,idPlanet):
    data = request.json
    me = FavoritePlanet(user_id=idUser, planet_id=idPlanet)
    db.session.add(me)
    db.session.commit()

    return jsonify({"mensaje": "Planeta añadido a favoritos"})

@api.route('<int:idUser>/favorite/character/<int:idCharacter>', methods=['DELETE'])
def delete_character(idUser,idCharacter):
    try:
        me = FavoriteCharacter.query.filter_by(user_id=idUser, character_id=idCharacter).one()
        db.session.delete(me)
        db.session.commit()
        message = {"message": "Personaje eliminado de favoritos"}
    except Exception as e:
        message = {"message": "El personaje no se encuentra en favoritos"}

    return jsonify(message)

@api.route('<int:idUser>/favorite/planet/<int:idPlanet>', methods=['DELETE'])
def delete_planet(idUser,idPlanet):
    try:
        me = FavoritePlanet.query.filter_by(user_id=idUser, planet_id=idPlanet).one()
        db.session.delete(me)
        db.session.commit()
        message = {"message": "Planeta eliminado de favoritos"}
    except Exception as e:
        message = {"message": "El planeta no se encuentra en favoritos"}

    return jsonify(message)
