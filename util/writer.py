import os


def write_on_csv(file_path, directory_type, value):
    with open(file_path, mode='w') as file_to_write_on:
        # Needs implementation
        pass


def terminal_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
