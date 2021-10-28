import variable_storage.string_factory as str_f
from tools.observer.Writer import Writer


class Communicator:

    def __init__(self):
        self.writer = Writer()

    def ask_back(self, examples=None):
        self.writer.terminal_cleaner()
        self.handle_examples(examples)
        user_input = input(str_f.PERMISSION_TO_PROCEED)
        if user_input in str_f.POSITIVE_FEEDBACK:
            return True
        elif user_input in str_f.NEGATIVE_FEEDBACK:
            return False
        else:
            print(str_f.YES_OR_NO)
            self.ask_back(examples)

    def handle_examples(self, examples):
        if examples is not None and len(examples) > 0:
            print(str_f.FILE_EXAMPLES_PROMPT)
            self.writer.display_examples(examples)
        else:
            print(str_f.EMPTY_DIR)
