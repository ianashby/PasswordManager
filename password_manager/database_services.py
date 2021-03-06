from password_manager.database_client import collection
from password_manager.password_hashing import PasswordHasher

class DatabaseServices:

    def __init__(self) -> None:
        self.PasswordHasher = PasswordHasher()

    def query_one(self, query_input):
        """
        Query/search for record based on account name input.

        Parameters:
            query_input(str): The name of the account that will be queried. 

        Returns:
            post(cursor): Cursor object that can be unpacked to view the query result.
            post_count(int): Integer of posts returned in query. 
        """
        try:
            post = collection.find({"account_name": query_input})
            post_count = collection.count_documents({"account_name": query_input})
            return post, post_count
        except Exception:
            print("Unable to find account in database.")
            print("\n\n")

    def query_many(self):
        """
        Query all records with the database.

        Returns:
            post(cursor): Cursor object that can be unpacked to view the query result.
            post_count(int): Integer of posts returned in query.
        """
        try:
            posts = collection.find({})
            post_count = collection.count_documents({})
            return posts, post_count
        except Exception:
            print("Unable to find passwords in database.")
            print("\n\n")


    def insert_post(self, account_name, account_address, email, username, password, date):
        """
        Insert a post into the database.

        Parameters:
            account_name(str): Name of account being added to database.
            account_address(str): Web address of account being added to database.
            email(str): Email associated with account being added to database.
            username(str): Username associated with account being added to database.
            password(str): Password associated with account being added to database.
            date(str): Date of when the post has been added to the database.
        """
        post = {
            "account_name": account_name,
            "account_address": account_address,
            "email": email,
            "username": username,
            "password": password,
            "date": date
        }

        try:
            collection.insert_one(post)
            print("Password was successfully added to the database.")
            print("\n\n")
        except Exception:
            print("Unable to insert record to database.")
            print("\n\n")


    def update_one(self, query_input, new_username, new_password, new_date):
        """
        Update a post's username and password by account name. 

        Parameters:
            query_input(str): Name of account being added to database.
            new_username(str): Username associated with account being added to database.
            new_password(str): Password associated with account being added to database.
            new_date(str): Date of when the post has been added to the database.
        """
        # Updating fan quantity form 10 to 25.
        filter = {"account_name": query_input}
        
        # Values to be updated.
        newvalues = {"$set": {"username": new_username, "password": new_password, "date": new_date}}

        try:
            collection.update_one(filter, newvalues)
            print(f"Username and password for {query_input} has successfully been updated!")
            print("\n\n")
        except Exception:
            print("Unable to update username and password.")
            print("\n\n")

    def delete_one(self, query_input):
        """
        Delete a post by account name.

        Parameters:
            query_input(str): Name of account being added to database.
        """
        try:
            collection.delete_one({"account_name": query_input})
            print(f"{query_input} has been deleted from the database.\n")
            print("\n\n")
        except Exception:
            print("Unable to delete all passwords from database.")
            print("\n\n")

    def delete_many(self):
        """
        Delete all posts in database.
        """
        try:
            collection.delete_many({})
            print("All passwords have been deleted from the database.")
            print("\n\n")
        except Exception:
            print("Unable to delete all passwords from database.")
            print("\n\n")

    def compare_password(self, account_input):
        """
        Returns True or False dependent on if input password matches the stored, hashed password.

        Parameters:
            account_input (str): The name of the account that will be used to compare the respective password.

        Returns:
            True/False (bool): Returns True if password matches hashed password. If not, returns False.
        """
        posts, post_count = self.query_one(account_input)
        
        if post_count > 0:
            for x in posts:
                post = x["password"]
        else:
            print("Unable to find account in database.")
            return False

        password_input = input("Password: ").encode()

        checked_pw = self.PasswordHasher.check_password(password_input, post)

        if checked_pw:
            print("Password validated!")
            return True