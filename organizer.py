import os


def observe_directory(file):
    print(f"{file} is a directory!")


def collect_downloads_content():
    downloads_path = "/home/moloch/Downloads"
    files = []
    for file_name in os.listdir(downloads_path):
        file = os.path.join(downloads_path, file_name)
        if os.path.isfile(file):
            files.append(file)
        if os.path.isdir(file):
            observe_directory(file)
    return files


def distribute(files):
    for file in files:
        print(file)


def define_paths():
    pass


def organize():
    define_paths()
    distribute(collect_downloads_content(d))


if __name__ == '__main__':
    organize()
