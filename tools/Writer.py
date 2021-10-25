import os
from variable_storage import magic_numbers as magic_ns, string_factory as str_f


class Writer:

    @staticmethod
    def write_on_csv(file_path, directory_type, value):
        with open(file_path, mode='w') as file_to_write_on:
            # ToDo This needs implementation
            pass

    @staticmethod
    def terminal_cleaner():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_examples(examples):
        for printing in range(magic_ns.ASSURANCE_PRINTING_DURATION):
            print("*" + examples[printing].split("/")[-1])
