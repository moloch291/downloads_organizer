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
        self.writer = Writer()
        self.communicator = Communicator()
        self.handled = False
        self.directories = Reader.read_from_csv(str_f.PATHS_CSV_PATH)

    def set_handled(self):
        self.handled = True

    def is_assured(self, directory_type):
        for directory in self.directories:
            if directory[str_f.DIRECTORY_TYPE] == directory_type:
                return directory[str_f.IS_ASSURED] == str_f.TRUE

    def is_assured_all(self):
        return self.is_assured(str_f.DOWNLOADS) and \
               self.is_assured(str_f.MUSIC) and \
               self.is_assured(str_f.VIDEOS) and \
               self.is_assured(str_f.PICTURES)

    def init_paths(self):
        for directory in self.directories:
            content = []
            if directory[str_f.PATH] == str_f.UNKNOWN and directory[str_f.IS_ASSURED] != str_f.TRUE:
                dir_path = Reader.define_path(directory[str_f.DIRECTORY_TYPE])
                if File_H.fill_up_container(content, dir_path):
                    if self.communicator.ask_back(content):
                        self.writer.write_on_csv(
                            str_f.PATHS_CSV_PATH,
                            directory[str_f.DIRECTORY_TYPE],
                            dir_path,
                            str_f.TRUE
                        )

    def distribute_files(self):
        if self.is_assured_all():
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
            self.init_paths()
            self.distribute_files()
