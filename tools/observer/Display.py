import os
# Data store:
from variable_storage import magic_numbers as magic_ns


class Display:

    @staticmethod
    def clean_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_files(files_to_display):
        init_range = magic_ns.ASSURANCE_PRINTING_DURATION
        printing_range = Display.define_printing_range(init_range, len(files_to_display))
        for file in range(printing_range):
            print("* " + files_to_display[file].split("/")[-1])

########################################################################################################################
    # Used only inside object:
########################################################################################################################

    @staticmethod
    def define_printing_range(init_range, len_of_object):
        return init_range if init_range <= len_of_object else len_of_object
