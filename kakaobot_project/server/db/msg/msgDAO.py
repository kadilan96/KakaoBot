
def getMessage(db, msgData):
    room = msgData['room']

    inputData = msgData.copy()
    del inputData['room']
    del inputData['isGroupChat']
    
    db[room].insert_one(inputData)