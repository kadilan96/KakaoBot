from flask import Flask
from flask_restx import Resource, Api

from rest.msgApi import msgApi

from swagger.msg import Msg

app = Flask(__name__)
api = Api(app)

app.register_blueprint(msgApi, url_prefix='/msg')

api.add_namespace(Msg, '/msg')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)