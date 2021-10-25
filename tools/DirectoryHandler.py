from Organizer import define_path
from tools import Reader
from tools import Communicator
from variable_storage import string_factory


class DirectoryHandler:

    def __init__(self):
        self.reader = Reader.Reader()
        self.communicator = Communicator.Communicator(input("Please provide a user name!"))

    def categorize_subdirectories(self, subdir):
        # ToDo implementation needs to be done
        print(f"{subdir} is a directory!")

    def collect_downloads_content(self, dir_type_str):
        target_path = define_path(dir_type_str)
        files_in_target = []
        try:
            self.reader.collect_content(target_path, files_in_target)
            assurance = self.communicator.ask_back(
                files_in_target,
                dir_type_str,
                string_factory.FILE_EXAMPLES_PROMPT
            )
            if not assurance:
                self.collect_downloads_content()
        except FileNotFoundError:
            print(string_factory.FOLDER_NOT_FOUND)
            self.collect_downloads_content(dir_type_str)
        return files_in_target
