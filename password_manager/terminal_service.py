class TerminalService:

    def __init__(self, database_services) -> None:
        self._ds = database_services

    def run_program(self):

        done = False

        while not done:
            self.display_menu()
            user_input = self.get_input()

            if user_input == 1:
                self._ds.query_many()
            elif user_input == 2:
                self._ds.query_one()
            elif user_input == 3:
                self._ds.insert()
            elif user_input == 4:
                self._ds.update()
            elif user_input == 5:
                self._ds.delete_one()
            elif user_input == 6:
                self._ds.delete_one()
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
    
    def get_input(self):
        """
        This function will gather user input from the menu.
        """
        user_input = int(input('Choose one: '))
        return user_input