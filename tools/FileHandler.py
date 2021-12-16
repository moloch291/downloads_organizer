from tools.observer.Reader import Reader
from tools.observer.Writer import Writer
from tools.observer.Display import Display

from variable_storage import string_factory as str_f


class FileHandler:

    @staticmethod
    def handle_subdirectory(subdir):
        # ToDo implementation needs to be done
        print(f"{subdir} is a directory!")

    @staticmethod
    def fill_up_container(container, dir_path):
        writer = Writer()
        try:
            Reader.collect_content(dir_path, container)
            return True
        except FileNotFoundError:
            Display.terminal_cleaner()
            print(str_f.FOLDER_NOT_FOUND)
            return False

    @staticmethod
    def relocate(file):
        print(f"This function will relocate {file}!")
