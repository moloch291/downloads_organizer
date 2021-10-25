from tools import Writer
from variable_storage import string_factory as str_f, magic_numbers as magic_ns


class Communicator:

    def __init__(self, user_name):
        self.user_name = user_name
        self.file_writer = Writer.Writer()

    def ask_back(self, examples, directory_type, prompt):
        self.file_writer.terminal_cleaner()
        print(prompt)
        for printing in range(magic_ns.ASSURANCE_PRINTING_DURATION):
            print(examples[printing].split("/")[-1])
        user_input = input(str_f.PERMISSION_TO_PROCEED)
        if user_input in ["Y", "y", "Yes", "yes"]:
            self.file_writer.write_on_csv(
                str_f.IS_ASSURED_CSV_PATH,
                directory_type,
                str_f.TRUE
            )
            return True
        elif user_input in ["N", "n", "No", "no"]:
            return False
        else:
            print(str_f.YES_OR_NO)
            self.ask_back(examples, directory_type, prompt)
