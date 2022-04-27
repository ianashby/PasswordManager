import pymongo
from password_manager.secrets import conn_str

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client["password_manager"]
collection = db["accounts_and_passwords"]

# try:
#     print(client.server_info())
# except Exception:
#     print("Unable to connect to the server.")

# post1 = {"name":"ian"}

# collection.insert_one(post1)
# collection.delete_many({})