
def getMessage(db, msgData):
    room = msgData['room']

    inputData = msgData.copy()
    del inputData['room']

    db[room] = inputData