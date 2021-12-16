# Tools:
import os.path
# Tools:
from tools.Communicator import Communicator
from tools.FileHandler import FileHandler as File_H
from tools.observer.Reader import Reader
from tools.observer.Writer import Writer
# Variable storage:
from variable_storage import string_factory as str_f


class Organizer:

    def __init__(self):
        # Tools:
        self.writer = Writer()
        self.communicator = Communicator()
        # Boolean private field:
        self.handled = False
        # List of directories and their info:
        self.directories = Reader.read_from_csv(str_f.PATHS_CSV_PATH)

########################################################################################################################
    # Public:
########################################################################################################################

    def set_handled(self):
        self.handled = True

    def update_directories(self):
        self.directories = Reader.read_from_csv(str_f.PATHS_CSV_PATH)

    def distribute_files(self):
        if self.__is_assured_all():
            download_content = []
            downloads_path = Reader.define_path(str_f.DOWNLOADS)
            Reader.collect_content(downloads_path, download_content)
            for file in download_content:
                if os.path.isfile(downloads_path + "/" + file):
                    File_H.relocate(file)
                if os.path.isdir(downloads_path + "/" + file):
                    File_H.handle_subdirectory(file)
            self.set_handled()
        else:
            self.__init_paths()
            self.distribute_files()

    def wants_to_redefine_paths(self):
        _wants_to = str(input("Do you want to choose new target folders? "))
        if _wants_to in str_f.POSITIVE_FEEDBACK:
            for dir_type in [str_f.DOWNLOADS, str_f.MUSIC, str_f.PICTURES, str_f.MUSIC, str_f.VIDEOS]:
                self.writer.write_on_csv(
                    str_f.PATHS_CSV_PATH,
                    dir_type,
                    str_f.UNKNOWN,
                    str_f.FALSE
                )
        elif _wants_to in str_f.NEGATIVE_FEEDBACK:
            print(str_f.WHATEVER)

########################################################################################################################
    # Private:
########################################################################################################################

    def __is_assured(self, directory_type):
        for directory in self.directories:
            if directory[str_f.DIRECTORY_TYPE] == directory_type:
                return directory[str_f.IS_ASSURED] == str_f.TRUE

    def __is_assured_all(self):
        return self.__is_assured(str_f.DOWNLOADS) and \
               self.__is_assured(str_f.MUSIC) and \
               self.__is_assured(str_f.VIDEOS) and \
               self.__is_assured(str_f.PICTURES)

    def __init_paths(self):
        for directory in self.directories:
            dir_path = Reader.define_path(directory[str_f.DIRECTORY_TYPE])
            content = []
            if directory[str_f.PATH] == str_f.UNKNOWN and \
                    directory[str_f.IS_ASSURED] != str_f.TRUE and \
                    File_H.fill_up_container(content, dir_path):
                # in separate 'if' in order to keep the execution's flow smooth:
                if self.communicator.ask_back(content):
                    self.writer.write_on_csv(
                        str_f.PATHS_CSV_PATH,
                        directory[str_f.DIRECTORY_TYPE],
                        dir_path,
                        str_f.TRUE
                    )
        self.update_directories()
