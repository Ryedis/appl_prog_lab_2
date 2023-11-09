import os
import shutil
import csv

from script_1 import create_csv_file


def create_dir(dir_name: str) -> None:
    """
    Create a directory if it doesn't exist.

    Args:
        dir_name (str): The name of the directory.
    """
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def copy_dir(dir_name: str) -> None:
    """
    Copy files from source directory to destination directory.

    Args:
        dir_name (str): The name of the destination directory.
    """
    create_dir(dir_name)
    for class_name in os.listdir('dataset'):
        list_name = os.listdir(os.path.join('dataset', (class_name)))
        for file_name in list_name:
            shutil.copyfile(
                os.path.join(os.path.join('dataset', class_name), file_name),
                os.path.join(dir_name, f"{class_name}_{file_name}")
            )


def write_in_csv(name_csv: str, dir_name: str) -> None:
    """
    Write file information to a CSV file.

    Args:
        name_csv (str): The name of the CSV file.
        dir_name (str): The name of the directory containing the files.
    """
    absolute_path = os.path.abspath(dir_name)
    relative_path = os.path.relpath(dir_name)
    file_name = os.listdir(dir_name)
    with open(name_csv, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for name in file_name:
            writer.writerow([
                os.path.join(absolute_path, name),
                os.path.join(relative_path, name),
                name.split("_")[0]
            ])


def main() -> None:
    copy_dir('dataset_copy_1')
    create_csv_file('annotation_2.csv')
    write_in_csv('annotation_2.csv', 'dataset_copy_1')


if __name__ == "__main__":
    main()