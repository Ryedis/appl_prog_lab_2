import os
import csv


def create_csv_file(name_file: str) -> None:
    """
    Create a CSV file with the given name.

    Args:
        name_file (str): The name of the CSV file.
    """
    with open(name_file, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["absolute_path", "relative_path", "class_label"])


def write_in_csv(name_csv: str, class_label: str) -> None:
    """
    Write data to an existing CSV file.

    Args:
        name_csv (str): The name of the CSV file to write to.
        class_label (str): The class label for the data.
    """
    absolute_path = os.path.abspath('dataset')
    relative_path = os.path.relpath('dataset')
    name_file = os.listdir(os.path.join(absolute_path, class_label))
    with open(name_csv, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for name in name_file:
            writer.writerow([os.path.join(absolute_path, class_label, name), os.path.join(relative_path, class_label, name), class_label])


def main() -> None:
    create_csv_file('annotation_1.csv')
    write_in_csv('annotation_1.csv', 'tiger')
    write_in_csv('annotation_1.csv', 'leopard')


if __name__ == "__main__":
    main()