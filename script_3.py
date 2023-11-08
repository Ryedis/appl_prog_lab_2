import os
import csv
import shutil
from random import sample

from script_1 import create_csv_file
from script_2 import create_dir

def copy_dir(name_dir: str, name_csv: str) -> None:
    """Copy a directory and create a CSV file."""
    list_number = sample(list(range(10001)), 5005)
    create_dir(name_dir)
    absolute_path = os.path.abspath(name_dir)
    relative_path = os.path.relpath(name_dir)
    counter = 0
    for class_name in os.listdir('dataset'):
        list_name = os.listdir(os.path.join('dataset', class_name))
        for file_name in list_name:
            random_name = str(list_number[counter]).zfill(5)
            shutil.copy(os.path.join(os.path.join('dataset', class_name), file_name),
                        os.path.join(name_dir, random_name + '.jpeg'))
            with open(name_csv, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([os.path.join(absolute_path, random_name + '.jpeg'),
                                 os.path.join(relative_path, random_name + '.jpeg'), class_name])
                counter+=1

def main() -> None:
    create_csv_file('annotation_3.csv')
    copy_dir('dataset_copy_2', 'annotation_3.csv')

if __name__ == "__main__":
    main()