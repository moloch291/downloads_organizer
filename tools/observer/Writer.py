import os
import csv
from variable_storage import magic_numbers as magic_ns, string_factory as str_f
from tools.observer.Reader import Reader


class Writer:

    def __init__(self):
        self.reader = Reader()

    def write_on_csv(self, file_path, directory_type, path, value):
        print("Writer called!")
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

    def terminal_cleaner(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_examples(self, examples):
        init_range = magic_ns.ASSURANCE_PRINTING_DURATION
        printing_range = init_range if init_range <= len(examples) else len(examples)
        for printing in range(printing_range):
            print("* " + examples[printing].split("/")[-1])
