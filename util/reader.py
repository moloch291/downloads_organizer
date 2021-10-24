import csv
import os


def read_from_csv(file_path):
    with open(file_path, mode='r') as file:
        paths_file = csv.DictReader(file)
        output = []
        for line in paths_file:
            output.append(line)
        return output


def content_collector(directory_path, file_container):
    for file_name in os.listdir(directory_path):
        file_container.append(file_name)
