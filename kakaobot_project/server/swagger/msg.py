from flask import request
from flask_restx import Resource, Namespace, fields

Msg = Namespace(
    name="/msg",
    description="카톡 메시지 기록용 API"
)

@Msg.route('/get-message')
class GetMessage(Resource):
    @Msg.expect(Msg.model('GetMessage', {
        "room": fields.String(required=True, description="Room"),
        "sender": fields.String(required=True, description="Sender"),
        "hash": fields.String(required=True, description="Sender's HashCode"),
        "msg": fields.String(required=True, description="message"),
        "isGroupChat": fields.Boolean(required=True, description="isGroupChat")
    }))
    def post(self):
        pass