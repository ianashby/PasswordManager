# Password Manager

---

# Overview

This project is a password manager that stores its data in a MongoDB cloud database. To run this program, run the main.py file. This will work with many other files within the password_manager folder to run the program. For example, database_services.py handles all of the basic database functions (query, insert, update, delete) and terminal_services.py handles what is printed in the terminal and gathers user input. Running the program will prompt you for various inputs. First you will be shown a menu where you can choose what you would like to do to the database. Dependent on your selection, you will be guided on what comes next. 

I chose to write this software to learn more about how to implement and work with cloud databases. I wanted to learn about the functionality of a cloud database and how Python could be used to accomplish the tasks of working with the cloud database. After this project, I can confidently say that I feel comfortable with working with a cloud database.

[Software Demo Video](https://youtu.be/L767eazIk-4)

# Cloud Database

MongoDB offers a cloud database service that is very flexible, quick, and scalable. MongoDB works with over 10 languages, and the platform is continuing to quickly grow. MongoDB is a NoSQL database and it ["stores data in flexible, JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time."](https://www.mongodb.com/what-is-mongodb)

Since this is a cloud database, my database is stored in "cluster" on the east coast. I can have many databases on this cluster. The one I am using is classed password_manager. Within the database, I have a collection named accounts_and_passwords. This collection will store usernames, passwords, emails, etc. related to an account that you insert. A new collection is made for each new insertion.  

# Development Environment

**MongoDB, VS Code**
MongoDB offers many ways to view the databases you create - online or directly in VS Code. I utilized VS Code to view the database since I also used VS Code to develop the program in. 

**Python, BCrypt, PyMongo**
I utilized Python for this project as it is the language that I am most familiar with and it seemed that MongoDB had great resources available for it. PyMongo is a package that you can install to easily work with your MongoDB database to insert, query, update, and delete posts. 

I also used Bcrypt to hash the passwords, but have turned off that functionality for the sake of the scope of the project. As explained below, I plan to use this functionality for backend use. 

# Useful Websites

* [Python MongoDB Tutorial using PyMongo by Tech With Tim](https://www.youtube.com/watch?v=rE_bJl2GAY8&list=LL&index=1)
* [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/tutorial.html)
* [Password Hashing](https://blog.devgenius.io/password-hashing-with-python-f3148692e8b9)
* [Password Hashing w/ bcrypt](https://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python)

# Future Work

Currently, this project stores unhashed and insecure passwords in the cloud. In the future, it would be ideal to store these passwords in a safer manner.
This would especially be needed if this were to be used on the backend of a web app. However, for this scope of this project, I have decided to turn off the password hashing feature. If/when this code is adapted for backend use not related to a password manager, I can easily adapt this code to work in a safe manner.

Additionally, if I wanted to further expand upon the project, I could build a proper user interface to complete all of the tasks available in this project.