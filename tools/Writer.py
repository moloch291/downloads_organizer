import os


class Writer:

    @staticmethod
    def write_on_csv(file_path, directory_type, value):
        with open(file_path, mode='w') as file_to_write_on:
            # ToDo This needs implementation
            pass

    @staticmethod
    def terminal_cleaner():
        os.system('cls' if os.name == 'nt' else 'clear')
