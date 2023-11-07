import os

def get_elements(class_name):
    path = os.path.join("dataset", class_name)
    name_list = os.listdir(path)
    name_list.append(None)
    for i in range(len(name_list)):
        if name_list[i] is not None:
            yield os.path.join(class_name, name_list[i])
        else:
            yield None

def main():
    print(*get_elements('tiger'))

if __name__ == "__main__":
    main()