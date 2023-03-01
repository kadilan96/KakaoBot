from db.connection import dbConnectionDAO as connDao

from db.msg import msgDAO as msgDao

db_name = "bot"

def getMessage(msgData):
    db = connDao.getDb(db_name)

    msgDao.getMessage(db, msgData)

    return {'result': 'success'}