import csv
import os

from variable_storage import string_factory


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
    def content_collector(directory_path, file_container):
        for file_name in os.listdir(directory_path):
            file_container.append(file_name)

    @staticmethod
    def find_searched_item(paths, path_of_):
        return [directory_path[string_factory.PATH] for directory_path in paths
                if directory_path[string_factory.DIRECTORY_TYPE] == path_of_][0]
