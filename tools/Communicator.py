import variable_storage.string_factory as str_f
from tools.observer.Writer import Writer


class Communicator:

    @staticmethod
    def ask_back(examples=None):
        Writer.terminal_cleaner()
        Communicator.handle_examples(examples)
        user_input = input(str_f.PERMISSION_TO_PROCEED)
        if user_input in str_f.POSITIVE_FEEDBACK:
            return True
        elif user_input in str_f.NEGATIVE_FEEDBACK:
            return False
        else:
            print(str_f.YES_OR_NO)
            return False

    @staticmethod
    def handle_examples(examples):
        if examples is not None and len(examples) > 0:
            print("\nThe target folder contains files such as:\n")
            Writer.display_examples(examples)
        else:
            print("\nThis directory is empty!")
