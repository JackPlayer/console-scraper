from columnar import columnar

def print_table(name, raw_data):
    formatted_data = convert_to_lists(raw_data)
    formatted_data_modified_bools = bool_to_string_list(formatted_data)
    print(formatted_data_modified_bools)
    table = columnar(formatted_data_modified_bools, headers=['PRICE', 'IN STOCK', 'RETAILER'], no_borders=True)

    print(name)
    print(table)

def dict_to_list(dict):
    new_list = []
    for value in dict: 
        new_list.append(dict[value])
    return new_list

def convert_to_lists(list_with_dicts):
    new_list = []
    for entry in list_with_dicts:
        if type(entry) is dict:
            new_list.append(dict_to_list(entry))
    return new_list

def bool_to_string(bool):
    return 'Yes' if bool else 'No'

def bool_to_string_list(list):
    list_copy = list.copy()
    for i,entry in enumerate(list):
        if entry == None: 
            continue
        for j, value in enumerate(entry):
            if type(value) is bool:
                list_copy[i][j] = bool_to_string(value)
    return list_copy

