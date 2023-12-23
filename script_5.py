import os
import csv


class IteratorDataset:
    def __init__(self, class_name: str) -> None:
        """
        Initializes an IteratorDataset object.

        Args:
            class_name (str): The name of the class for the dataset.
        """
        self.file_names = os.listdir(os.path.join('dataset', class_name))
        self.len = len(self.file_names)
        self.class_name = class_name
        self.counter = 0


    def __next__(self) -> str:
        """
        Returns the next file path in the dataset.

        Returns:
            str: The file path.
        
        Raises:
            StopIteration: If there are no more file paths to return.
        """
        if self.counter < self.len:
            self.counter += 1
            return os.path.join(self.class_name, self.file_names[self.counter-1])
        else:
            raise StopIteration


class IteratorCopyDataset:
    def __init__(self, class_name: str, dir_name: str) -> None:
        """
        Initializes an IteratorCopyDataset object.

        Args:
            class_name (str): The name of the class from the dataset.
            dir_name (str): The name of the directory containing the dataset files.
        """
        self.file_names = []
        for name in os.listdir(dir_name):
            if class_name == name[0]:
                self.file_names.append(name)
                
        self.len = len(self.file_names)
        self.class_name = class_name
        self.counter = 0        


    def __next__(self) -> str:
        """
        Returns the next file path in the copied dataset.

        Returns:
            str: The file path.
        
        Raises:
            StopIteration: If there are no more file paths to return.
        """
        if self.counter < self.len:
            self.counter += 1
            return os.path.join(self.file_names[self.counter-1])
        else:
            raise StopIteration


def print_iterator(name: str, count: int) -> None:
    """
    Prints the next elements from an IteratorDataset.

    Args:
        name (str): The name of the IteratorDataset.
        count (int): count of elements
    Returns:
        None
    """
    a = IteratorDataset(name)
    for i in range(count):
        print(next(a))

def main() -> None :
    """
    Calls the print_iterator function with name.
    Args:
        None
    Returns:
        None
    """
    print_iterator("tiger", 2000)


if __name__ == "__main__":
    main()