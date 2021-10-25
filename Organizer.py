# Tools:
from tools import Reader as rdr, Writer, Communicator, DirectoryHandler as dir_h

# Variable storage:
from variable_storage import string_factory
from variable_storage import magic_numbers

# Will become class...
reader = rdr.Reader()
writer = Writer.Writer()


def is_assured(directory_type):
    permissions = reader.read_from_csv(string_factory.IS_ASSURED_CSV_PATH)
    for permission in permissions:
        if permission[string_factory.DIRECTORY_TYPE] == directory_type:
            return permission[string_factory.VALUE] == string_factory.TRUE


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
    output_path_in_file = reader.find_searched_item(paths, path_of_)
    output_path = output_path_in_file if output_path_in_file != string_factory.UNKNOWN \
        else input(f"The '{path_of_}' folder path unknown! Please provide: ")
    return output_path


def organize():
    handler = dir_h.DirectoryHandler()
    content = handler.collect_downloads_content(string_factory.DOWNLOADS)
    if len(content) > 0:
        distribute(content)


if __name__ == '__main__':
    organize()
