# Accessing tools:
from tools.observer.Reader import Reader
from tools.observer.Display import Display
# Make variables available:
from variable_storage import string_factory as str_f


class FileHandler:

    # Read and distribute directory in Downloads:
    @staticmethod
    def handle_subdirectory(subdir):
        # ToDo implementation needs to be done
        print(f"{subdir} is a directory!")

    # Read directory content and fill the container with it:
    @staticmethod
    def fill_up_container(container, dir_path):
        try:
            Reader.collect_content(dir_path, container)
            return True
        except FileNotFoundError:
            Display.clean_console()
            print(str_f.FOLDER_NOT_FOUND)
            return False

    # Relocate the file:
    @staticmethod
    def relocate(file):
        print(f"This function will relocate {file}!")
