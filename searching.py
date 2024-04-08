import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    #načtení klíčů a ověření zda je klíč reálný
    with open(file_name, mode = "r") as f:
        allowed_keys = json.load(f)
    if field not in allowed_keys:
        return None

    # načtení dat
    with open(file_path, "r") as f:
        data = json.load(f)
    return data.get(field, None)


def main():
    data = read_data("sequential.json", "unordered_numbers")
    print(data)


if __name__ == '__main__':
    main()