import os
import csv

def create_csv_file(name_file):
    with open(name_file, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["absolute_path", "relative_path", "class_label"])

def write_in_csv(name_csv, class_label):
    absolute_path = os.path.abspath('dataset')
    relative_path = os.path.relpath('dataset')
    name_file = os.listdir(os.path.join(absolute_path, class_label))
    with open(name_csv, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for name in name_file:
            writer.writerow([os.path.join(absolute_path, class_label, name), os.path.join(relative_path, class_label, name), class_label])

def main():
    create_csv_file('annotation_1.csv')
    write_in_csv('annotation_1.csv', 'tiger')
    write_in_csv('annotation_1.csv', 'leopard')

if __name__ == "__main__":
    main()