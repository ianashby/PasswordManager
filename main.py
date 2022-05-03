from password_manager.terminal_service import TerminalService
from password_manager.database_client import collection

def main():
    director = TerminalService()
    director.run_program()

if __name__ == "__main__":
    main()