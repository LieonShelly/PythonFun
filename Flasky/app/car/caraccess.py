from app.car import car_api
from app.car.documet import CarBrand
from flask import jsonify

@car_api.route('/brandlist')
def brandlist():
   brands = CarBrand.objects[:5]
   json_data = brands.to_json()
   return jsonify(json_data)


@car_api.route('/')
def index():
   return jsonify({"index": "success"})
