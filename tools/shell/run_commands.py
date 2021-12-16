import os


def cut_file(file_name, path_origin, destination_path):
    os.system(
        f"cp {path_origin} {destination_path}/{file_name} && rm {path_origin}"
    )


def cut_dir(dir_path, destination_path):
    os.system(
        f"cp -r {dir_path} {destination_path} && rm -r {dir_path}"
    )
