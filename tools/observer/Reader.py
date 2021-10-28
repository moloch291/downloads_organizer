import csv
import os

from variable_storage import string_factory as str_f


class Reader:

    @staticmethod
    def read_from_csv(file_path):
        with open(file_path, mode='r') as file:
            paths_file = csv.DictReader(file)
            output = []
            for line in paths_file:
                output.append(line)
            return output

    @staticmethod
    def collect_content(directory_path, container):
        for file_name in os.listdir(directory_path):
            container.append(file_name)

    @staticmethod
    def find_searched_item(paths, path_of_):
        return [directory_path[str_f.PATH]
                for directory_path in paths
                if directory_path[str_f.DIRECTORY_TYPE] == path_of_][0]

    @staticmethod
    def define_path(path_of_):
        paths = Reader.read_from_csv(str_f.PATHS_CSV_PATH)
        output_path_in_file = Reader.find_searched_item(paths, path_of_)
        output_path = output_path_in_file if output_path_in_file != str_f.UNKNOWN \
            else input(f"The '{path_of_}' folder path unknown! Please provide: ")
        return output_path
