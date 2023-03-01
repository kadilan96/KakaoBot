from flask import request, jsonify
from flask import Blueprint

from db import msgDB as db

msgApi = Blueprint("msg", __name__)

@msgApi.route('/get-message', methods=['POST'])
def post_getMessage():
    param = request.get_json()
    result = db.getMessage(param)

    return jsonify(result)