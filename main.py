from password_manager.terminal_service import TerminalService
from password_manager.database_services import DatabaseServices

def main():

    director = TerminalService()
    director.run_program()

if __name__ == "__main__":
    main()