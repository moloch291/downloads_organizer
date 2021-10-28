import os
import csv
from variable_storage import magic_numbers as magic_ns, string_factory as str_f
from tools.observer.Reader import Reader


class Writer:

    @staticmethod
    def write_on_csv(file_path, directory_type, path, value):
        print("Writer called!")
        contents = Reader.read_from_csv(file_path)
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

    @staticmethod
    def terminal_cleaner():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_examples(examples):
        init_range = magic_ns.ASSURANCE_PRINTING_DURATION
        printing_range = init_range if init_range <= len(examples) else len(examples)
        for printing in range(printing_range):
            print("* " + examples[printing].split("/")[-1])
