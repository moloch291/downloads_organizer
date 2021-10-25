from tools import Reader, Communicator, Writer
from variable_storage import string_factory as str_f


class DirectoryHandler:

    def __init__(self):
        self.communicator = Communicator.Communicator(input("Please provide a user name: "))

    def categorize_subdirectories(self, subdir):
        # ToDo implementation needs to be done
        print(f"{subdir} is a directory!")

    def collect_content_of_target_dir(self, dir_type_str):
        target_path = Reader.Reader.define_path(dir_type_str)
        files_in_target = []
        try:
            Reader.Reader.collect_content(target_path, files_in_target)
            if not self.communicator.ask_back(dir_type_str, "\n" + str_f.FILE_EXAMPLES_PROMPT, files_in_target):
                return self.collect_content_of_target_dir(dir_type_str)
            Writer.Writer.write_on_csv(
                str_f.IS_ASSURED_CSV_PATH,
                dir_type_str,
                str_f.TRUE
            )
        except FileNotFoundError:
            print(str_f.FOLDER_NOT_FOUND)
            return self.collect_content_of_target_dir(dir_type_str)
        return files_in_target
