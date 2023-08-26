import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017")
db=myclient["ocean"]
col=db["student details"]
data={"name":"Rathish","Age":17,"mark":450}
col.insert_one(data)
print("inserted")
