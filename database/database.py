import pymongo, os
from config import DB_URI


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient["USERs"]


user_data = database['Free']
pro_data = database['Pro']


async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return



async def present_pro_user(user_id : int):
    found = pro_data.find_one({'_id': user_id})
    return bool(found)

async def add_pro_user(user_id: int, name: str, uname: str, date: int):
    pro_data.insert_one({
        '_id': user_id,
        'Name': name,
        '@': uname,
        'Date': date
    })
    return

async def full_pro_userbase():
    user_docs = pro_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_pro_user(user_id: int):
    pro_data.delete_one({'_id': user_id})
    return
