import pymongo, os
from config import DB_URI


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient["USERs"]
user_data = database['Uids']

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


prodatabase = dbclient["PREMIUM"]
pro_user = prodatabase["Info"]

async def present_PROuser(user_id : int):
    found = pro_user.find_one({'_id': user_id})
    return bool(found)

async def add_PROuser(fullname: str, user_id: int, Username: str, DaTe: int):
    pro_user.insert_one({
        '_name': fullname,
        '_id': user_id,
        '_@': Username,
        '_date': DaTe
    })
    return

async def full_PROuserbase():
    user_docs = pro_user.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_PROuser(user_id: int):
    pro_user.delete_one({'_id': user_id})
    return
