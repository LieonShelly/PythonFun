from app.car import car_api
from app.car.documet import CarBrand
from flask import jsonify
import json
from mongoengine.queryset.visitor import Q


@car_api.route('/brandlist')
def brandlist():
   # brands = CarBrand.objects()
   # json_data = json.loads(brands.to_json())
   # return jsonify(json_data)

   brands = CarBrand.objects(Q(letter='A') | Q(letter='B'))
   json_data = json.loads(brands.to_json())
   return jsonify(json_data)


@car_api.route('/')
def index():
   return jsonify({"index": "success"})
