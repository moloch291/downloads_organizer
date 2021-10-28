import csv
# Import variables:
from variable_storage import string_factory as str_f
# import Reader:
from tools.observer.Reader import Reader


class Writer:

    def __init__(self):
        self.reader = Reader()

    def write_on_csv(self, file_path, directory_type, path, value):
        contents = self.reader.read_from_csv(file_path)
        with open(file_path, mode='w', newline='') as file_to_write_on:
            field_names = [str_f.DIRECTORY_TYPE, str_f.PATH, str_f.IS_ASSURED]
            writer = csv.DictWriter(file_to_write_on, fieldnames=field_names)
            writer.writeheader()
            for line in contents:
                if line[str_f.DIRECTORY_TYPE] != directory_type:
                    writer.writerow(line)
                else:
                    writer.writerow({
                        str_f.DIRECTORY_TYPE: directory_type,
                        str_f.PATH: path,
                        str_f.IS_ASSURED: value
                    })
