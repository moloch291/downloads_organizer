import variable_storage.string_factory as str_f
from tools.observer.Writer import Writer


def handle_examples(examples):
    if examples is not None and len(examples) > 0:
        print("\nThe target folder contains files such as:\n")
        Writer.display_examples(examples)
    else:
        print("\nThis directory is empty!")


class Communicator:

    def __init__(self, user_name=None):
        self.user_name = input("Please provide a user name: ") if user_name is None else user_name

    def ask_back(self, directory_type, prompt, examples=None):
        Writer.terminal_cleaner()
        handle_examples(examples)
        user_input = input(str_f.PERMISSION_TO_PROCEED)
        if user_input in str_f.POSITIVE_FEEDBACK:
            return True
        elif user_input in str_f.NEGATIVE_FEEDBACK:
            return False
        else:
            print(str_f.YES_OR_NO)
            return self.ask_back(directory_type, prompt, examples)
