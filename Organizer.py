# Tools:
import os.path

from tools import Communicator
from tools.DirectoryHandler import DirectoryHandler as Dir_H
from tools.observer.Reader import Reader
from tools.observer.Writer import Writer

# Variable storage:
from variable_storage import string_factory as str_f


def is_assured(directory_type):
    directories = Reader.read_from_csv(str_f.PATHS_CSV_PATH)
    for directory in directories:
        if directory[str_f.DIRECTORY_TYPE] == directory_type:
            return directory[str_f.IS_ASSURED] == str_f.TRUE


def is_assured_all():
    return is_assured(str_f.DOWNLOADS) and \
           is_assured(str_f.MUSIC) and \
           is_assured(str_f.VIDEOS) and \
           is_assured(str_f.PICTURES)


def init_paths(user_name=None):
    communicator = Communicator.Communicator(user_name)
    directories = Reader.read_from_csv(str_f.PATHS_CSV_PATH)
    for directory in directories:
        content = []
        if directory[str_f.PATH] == str_f.UNKNOWN or directory[str_f.IS_ASSURED] != str_f.TRUE:
            dir_path = Reader.define_path(directory[str_f.DIRECTORY_TYPE])
            fill_up_content(content, dir_path, communicator.user_name)
            if communicator.ask_back(directory[str_f.DIRECTORY_TYPE], str_f.FILE_EXAMPLES_PROMPT, content):
                Writer.write_on_csv(
                    str_f.PATHS_CSV_PATH,
                    directory[str_f.DIRECTORY_TYPE],
                    dir_path,
                    str_f.TRUE
                )


def fill_up_content(content, dir_path, user_name):
    try:
        Reader.collect_content(dir_path, content)
    except FileNotFoundError:
        Writer.terminal_cleaner()
        print(str_f.FOLDER_NOT_FOUND)
        init_paths(user_name)


def distribute_files():
    if is_assured_all():
        download_content = []
        Reader.collect_content(Reader.define_path(str_f.DOWNLOADS), download_content)
        for file in download_content:
            relocate(file) if os.path.isfile(file) else Dir_H.handle_subdirectories(file)
            print(file)
    else:
        init_paths()


def relocate(file):
    print("This function will relocate a given file!")


if __name__ == '__main__':
    distribute_files()
