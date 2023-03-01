from pymongo import MongoClient

def getClient(url='localhost', post=27017):
    client = MongoClient(url, post)
    
    print('MongoDB Connected')

    return client

def getDb(dbName, client=getClient()):
    db = client[dbName]

    return db

def checkNotExist(db, collectionName):
    return True if not collectionName in db.list_collection_names() else False

def createDb(db, collectionName, client=getClient()):
    if checkNotExist(db, collectionName):
        _ = db[collectionName]
