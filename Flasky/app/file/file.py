from app.file import file_api
from app import photos
from flask import request, jsonify

@file_api.route('/upload', methods=['POST'])
def upload():
    filename = photos.save(request.files['photo'])
    file_url = photos.url(filename)
    return jsonify({"url": file_url})
