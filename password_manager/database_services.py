from password_manager.database_client import collection

class DatabaseServices:

    def query_one(self, query_input):
        """
        Query/search for record based on account name input.
        """
        try:
            post = collection.find({"account_name": query_input})
            post_count = collection.count_documents({"account_name": query_input})
            return post, post_count
        except Exception:
            print("Unable to find account in database.")

    def query_many(self):
        """
        Query all records with the database.
        """
        try:
            posts = collection.find({})
            post_count = collection.count_documents({})
            return posts, post_count
        except Exception:
            print("Unable to find passwords in database.")


    def insert_post(self, account_name, account_address, email, username, password, date):
        """
        Insert a post into the database.
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
        except Exception:
            print("Unable to insert record to database.")


    def update_one(self, query_input, new_username, new_password, new_date):
        """
        Update a post's username and password by account name. 
        """
        # Updating fan quantity form 10 to 25.
        filter = {"account_name": query_input}
        
        # Values to be updated.
        newvalues = {"$set": {"username": new_username, "password": new_password, "date": new_date}}

        try:
            collection.update_one(filter, newvalues)
            print(f"Username and password for {query_input} has successfully been updated!")


        except Exception:
            print("Unable to update username and password.")

    def delete_one(self, query_input):
        """
        Delete a post by account name.
        """
        try:
            collection.delete_one({"account_name": query_input})
            print(f"{query_input} has been deleted from the database.\n")
        except Exception:
            print("Unable to delete all passwords from database.")

    def delete_many(self):
        """
        Delete all posts in database.
        """
        try:
            collection.delete_many({})
            print("All passwords have been deleted from the database.\n")
        except Exception:
            print("Unable to delete all passwords from database.")