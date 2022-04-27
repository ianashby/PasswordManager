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
                posts = self._ds.query_many()
                self.print_table(posts)
            elif user_input == 2:
                self._ds.query_one()
            elif user_input == 3:
                self._ds.insert_post()
            elif user_input == 4:
                self._ds.update()
            elif user_input == 5:
                self._ds.delete_one()
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

    def print_table(self, posts):
        print("{:>15} {:>15} {:>15}".format("Account Name", "Web Address", "Email"))
        for post in posts:
            print("{:>15} {:>15} {:>15}".format(post["account_name"], post["account_address"], post["email"]))
    
    def get_input(self):
        """
        This function will gather user input from the menu.
        """
        user_input = int(input('Choose one: '))
        return user_input