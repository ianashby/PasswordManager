import datetime
from password_manager.database_client import collection

class DatabaseServices:

    def __init__(self) -> None:
        pass

    def query_one(self):
        pass

    def query_many(self):
        pass

    def insert(self):
        """
        Insert a post into the database.
        """

        account_name = input("Account name: ")
        account_address = input("Account web address: ")
        email = input("Email: ")
        username = input("Username: ")
        password = input("Password: ")
        date = str(datetime.date.today())
    
        post = {
            "account_name": account_name,
            "account_address": account_address,
            "email": email,
            "username": username,
            "password": password,
            "date": date
        }

        return collection.insert_one(post)

    def update(self):
        pass

    def delete_one(self):
        pass

    def delete_many(self):
        pass

