import datetime
from password_manager.database_services import DatabaseServices

class TerminalService:

    def __init__(self) -> None:
        self._ds = DatabaseServices()

    def run_program(self):

        done = False

        while not done:
            self.display_menu()
            user_input = self.get_input()

            if user_input == 1:
                posts, post_count = self._ds.query_many()
                self.print_table(posts, post_count)

            elif user_input == 2:
                account_name = input("Account name: ")
                post, post_count = self._ds.query_one(account_name)
                self.print_table(post, post_count)

            elif user_input == 3:
                account_name = input("Account name: ")
                account_address = input("Account web address: ")
                email = input("Email: ")
                username = input("Username: ")
                password = input("Password: ")
                date = str(datetime.date.today())
                self._ds.insert_post(account_name, account_address, email, username, password, date)

            elif user_input == 4:
                account_name = input("Account name: ")
                post, post_count = self._ds.query_one(account_name)
                if post_count > 0:
                    new_username = input("New username: ")
                    new_password = input("New password: ")
                    new_date = str(datetime.date.today())
                    self._ds.update_one(account_name, new_username, new_password, new_date)
                else:
                    print("nope")

            elif user_input == 5:
                account_name = input("Account name: ")
                self._ds.delete_one(account_name)

            elif user_input == 6:
                self._ds.delete_many()

            elif user_input == 7:
                print("Goodbye!")
                done = True

    def display_menu(self):
        """
        This function will display the terminal menu.
        """
        print('-'*30)
        print(('-'*12) + ' Menu '+ ('-' *12))
        print('1. View all passwords')
        print('2. Search for password')
        print('3. Insert new password')
        print('4. Update password')
        print('5. Delete password')
        print('6. Delete all passwords')
        print('7. Quit')
        print('-'*30)

    def print_table(self, posts, post_count):
        print("\n\n")

        if post_count > 0:
            print("{:>15} {:>15} {:>15} {:>15} {:>15} {:>15}".format("Account Name", "Web Address", "Email", "Username", "Password", "Date"))

            for post in posts:
                print("{:>15} {:>15} {:>15} {:>15} {:>15} {:>15}".format(post["account_name"], post["account_address"], post["email"], post["username"], post["password"], post["date"]))

        else:
            print("No records to display.")
        print("\n\n")


    def get_input(self):
        """
        This function will gather user input from the menu.
        """
        user_input = int(input('Choose one: '))
        return user_input