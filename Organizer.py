# Tools:
from tools import Reader as rdr
from tools import Writer
# Variable storage:
from variable_storage import string_factory
from variable_storage import magic_numbers

# Will become class...
reader = rdr.Reader()


def is_assured(directory_type):
    permissions = reader.read_from_csv(string_factory.IS_ASSURED_CSV_PATH)
    for permission in permissions:
        if permission[string_factory.DIRECTORY_TYPE] == directory_type:
            return permission[string_factory.VALUE] == string_factory.TRUE


def ask_back(examples, directory_type):
    file_writer = Writer.Writer()
    file_writer.terminal_cleaner()
    print(string_factory.FILE_EXAMPLES_PROMPT)
    for printing in range(magic_numbers.ASSURANCE_PRINTING_DURATION):
        print(examples[printing].split("/")[-1])
    user_input = input(string_factory.PERMISSION_TO_PROCEED)
    if user_input in ["Y", "y", "Yes", "yes"]:
        file_writer.write_on_csv(
            string_factory.IS_ASSURED_CSV_PATH,
            directory_type,
            string_factory.TRUE
        )
    elif user_input in ["N", "n", "No", "no"]:
        collect_downloads_content()
    else:
        print(string_factory.YES_OR_NO)
        ask_back(examples, directory_type)


def collect_downloads_content():

    downloads_path = define_path(string_factory.DOWNLOADS)
    files_in_download = []
    try:
        reader.content_collector(downloads_path, files_in_download)
        ask_back(files_in_download, string_factory.DOWNLOADS)
    except FileNotFoundError:
        print(string_factory.FOLDER_NOT_FOUND)
        collect_downloads_content()
    return files_in_download


def is_assured_all():
    return is_assured(string_factory.DOWNLOADS) and \
           is_assured(string_factory.MUSIC) and \
           is_assured(string_factory.VIDEOS) and \
           is_assured(string_factory.PICTURES)


def distribute(downloads_content):
    if is_assured_all():
        for file in downloads_content:
            print(file)
    else:
        organize()


def define_path(path_of_):
    paths = reader.read_from_csv(string_factory.PATHS_CSV_PATH)
    output_path_in_file = [directory_path[string_factory.PATH]
                           for directory_path in paths
                           if directory_path[string_factory.DIRECTORY_TYPE] == path_of_][0]
    output_path = output_path_in_file if output_path_in_file != string_factory.UNKNOWN \
        else input(f"The '{path_of_}' folder path unknown! Please provide: ")
    return output_path


def organize():
    content = collect_downloads_content()
    if len(content) > 0:
        distribute(content)


if __name__ == '__main__':
    organize()
