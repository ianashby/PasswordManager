import datetime
from password_manager.database_client import collection

class DatabaseServices:

    def __init__(self) -> None:
        pass

    def query_one(self):
        """
        Query/search for record based on account name input.
        """
        pass

    def query_many(self):
        """
        Query all records with the database.
        """
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

        try:
            return collection.insert_one(post)
        except Exception:
            print("Unable to insert record to database.")


    def update(self):
        """
        Update a post by account name. 
        """
        pass

    def delete_one(self):
        """
        Delete a post by account name.
        """
        pass

    def delete_many(self):
        """
        Delete all posts in database.
        """
        pass

# TODO printing function?