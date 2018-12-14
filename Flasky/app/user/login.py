from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, jwt_refresh_token_required, \
	create_refresh_token

from app.user import user
from app.user.model import User, VerrifyStatus

@user.route('/')
def index():
	return "user index"


@user.route('/get')
@jwt_required
def get_user():
	current_user = get_jwt_identity()
	return  jsonify(current_user=current_user)

@user.route('/login', methods=['POST'])
def login():
	if not request.is_json:
		return jsonify({"msg": "Missing JSON in request"}), 400
	username = request.json.get("username")
	password = request.json.get('password')
	if not username:
		return jsonify({"msg": "Missing username parameter"}), 400
	if not password:
		return jsonify({"msg": "Missing password parameter"}), 400
	access_token = create_access_token(identity=username)
	refresh_token = create_refresh_token(identity=username)
	user = User(password="password")
	# user.username = "sdf"
	# user.password = "sadf"
	user.__dict__ = request.json
	user.status = VerrifyStatus.checking
	return  jsonify(user.__dict__) #jsonify(access_token=access_token, refresh_token=refresh_token)

@user.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
	current_user = get_jwt_identity()
	ret = {
		'access_token': create_access_token(identity=current_user, fresh=False)
	}
	return jsonify(ret), 200
