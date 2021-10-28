import os
# Data store:
from variable_storage import magic_numbers as magic_ns


class Display:

    @staticmethod
    def terminal_cleaner():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_examples(examples):
        init_range = magic_ns.ASSURANCE_PRINTING_DURATION
        printing_range = init_range if init_range <= len(examples) else len(examples)
        for printing in range(printing_range):
            print("* " + examples[printing].split("/")[-1])
