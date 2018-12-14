'''
	
'''
from app import mongod
from app.city import city_api
from flask import jsonify
import os
import json

@city_api.route('/', methods=['GET'])
def index():
	return "city index"


@city_api.route('/add', methods=['GET'])
def add_data():
	# 获取当前文件路径
	current_path = os.path.abspath(__file__)
	parent_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
	json_path = os.path.join(parent_path + os.path.sep + 'json')
	print("=====",json_path)

	with open(os.path.join(json_path + os.path.sep + "area.json"),'r', encoding='utf-8') as f:
		area_data = f.read()
		area_json = json.loads(area_data)
		mongod.db.area.insert(area_json)

	with open(os.path.join(json_path + os.path.sep + "city.json"),'r', encoding='utf-8') as f:
		area_data = f.read()
		area_json = json.loads(area_data)
		mongod.db.city.insert(area_json)


	with open(os.path.join(json_path + os.path.sep + "province.json"),'r', encoding='utf-8') as f:
		area_data = f.read()
		area_json = json.loads(area_data)
		mongod.db.province.insert_many(area_json)

	return  jsonify({"msg": "success"})
