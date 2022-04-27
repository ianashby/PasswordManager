from password_manager.terminal_service import TerminalService
from password_manager.database_services import DatabaseServices

def main():

    database_service = DatabaseServices()
    director = TerminalService(database_service)
    director.run_program()

if __name__ == "__main__":
    main()