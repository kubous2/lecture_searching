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

def linear_search(data,hledane_cislo):
    positions = []
    count = 0
    for i in range(len(data)):
        if data[i] == hledane_cislo:
            count+=1
            positions.append(i)
    slovnik = {"positions": positions, "count": count}
    return slovnik

def  pattern_search(data, vzor):
    velikost_vzoru = len(vzor) #3
    delka_data = len (data)
    positions = []
    count = 0
    for i in range(delka_data-velikost_vzoru+1):
        if data[i:i + velikost_vzoru] == vzor:
            count += 1
            positions.append(i)
    slovnik = {"positions": positions, "count": count}
    return slovnik

def binary_search(data, hledane_cislo):
    indexy = []
    for i in range (len(data)):
        if data[i] == hledane_cislo:
            indexy.append(i)
    if indexy == []:
        return None
    return indexy


def main():
    data = read_data("sequential.json", "unordered_numbers")
    l_search  = linear_search(data, 0)
    print (l_search)

    data = read_data("sequential.json", "dna_sequence")
    p_search = pattern_search(data,"ATA")
    print (p_search)

    data = read_data("sequential.json", "ordered_numbers")
    b_search = binary_search(data, 1)
    print (b_search)


if __name__ == '__main__':
    main()