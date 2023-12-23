import os
from typing import Generator, Optional


def get_elements(class_name: str) -> Generator[Optional[str], None, None]:
    """
    Get file elements in the specified class directory.

    Args:
        class_name (str): The name of the class.

    Yields:
        Optional[str]: The path of the file element or None.

    """
    path = os.path.join("dataset", class_name)
    name_list = os.listdir(path)
    name_list.append(None)
    for i in range(len(name_list)):
        if name_list[i] is not None:
            yield os.path.join(class_name, name_list[i])
        else:
            return None


def main() -> None :
    """
    Prints the elements by class_label
    Args:
        None
    Returns:
        None
    """
    print(*get_elements('tiger'))


if __name__ == "__main__":
    main()