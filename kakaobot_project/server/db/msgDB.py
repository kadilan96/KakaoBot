from db.connection import dbConnectionDAO as connDao

from db.msg import msgDAO as msgDao

db_name = "kakaoBot"

def getMessage(msgData):
    db = connDao.getDb(db_name)

    if msgData['isGroupChat']:
        msgDao.getMessage(db, msgData)

        return {'result': 'success'}
    else:
        return {'result': 'fail', 'error': 'NotGroupChatException'}