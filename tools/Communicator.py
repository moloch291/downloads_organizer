import variable_storage.string_factory as str_f
import observer.Writer as Writer


class Communicator:

    def __init__(self, user_name):
        self.user_name = user_name
        self.writer = Writer.Writer()

    def ask_back(self, directory_type, prompt, examples=None):
        if examples is None:
            examples = []
        self.writer.terminal_cleaner()
        print(prompt)
        if examples is not None:
            self.writer.display_examples(examples)
        user_input = input(str_f.PERMISSION_TO_PROCEED)
        if user_input in str_f.POSITIVE_FEEDBACK:
            return True
        elif user_input in str_f.NEGATIVE_FEEDBACK:
            return False
        else:
            print(str_f.YES_OR_NO)
            return self.ask_back(directory_type, prompt, examples)
