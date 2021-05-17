"""
User interface tabular printer
"""

from columnar import columnar


def print_table(name, raw_data):
    """Prints the name of the product, along with a tabular layout of the product information from various retailers
    
    Args:
        name (string): Name of the product
        raw_data (list): The product data in the form [{'price': '$599', 'in_stock': True, 'retailer':'bestbuy'}, ...]
    
    """
    print(format_name(name))

    if (len(raw_data) == 0):
        print("No data found")
        return

    formatted_data = convert_to_lists(raw_data)
    formatted_data_modified_bools = bool_to_string_list(formatted_data)
    table = columnar(formatted_data_modified_bools, headers=['PRICE', 'IN STOCK', 'RETAILER'], no_borders=True)
    print(table)

def format_name(raw_name):
    """Removes _ and URLS from raw_name 
    
    Args:
        raw_name(string): The name to format
    """
    return raw_name.replace('_', ' ').replace(' URLS', '')

def dict_to_list(dictionary):
    """ Converts a dict to a list where the items in the list are the values of the dict

    Args:
        dictionary(dict): Any dictionary 

    Returns:
        list: Of the values from the dict
    """
    new_list = []
    for value in dict: 
        new_list.append(dictionary[value])
    return new_list

def convert_to_lists(list_with_dicts):
    """ Converts a list containing dicts into a list of lists where the contents of the lists are the values from the dictionary. 

    Args:
        list_with_dicts(list): [{'key':'value'}...]

    Returns:
        list: [['value1', 'value2'], ['value1', 'value2']...]
    """
    new_list = []
    for entry in list_with_dicts:
        if type(entry) is dict:
            new_list.append(dict_to_list(entry))
    return new_list


def bool_to_string(bool):
    """ Converts True / False into 'Yes' / 'No'

    Returns:
        string: 'Yes' or 'No'
    """
    return 'Yes' if bool else 'No'

def bool_to_string_list(list):
     """ Converts True / False into 'Yes' / 'No' in a 2D list

    Args: 
        list: 2D list [[True, False], [True]] with True and False values

    Returns:
        list: 2D list [['Yes', 'No'], ['Yes']]
    """
    list_copy = list.copy()
    for i,entry in enumerate(list):
        if entry == None: 
            continue
        for j, value in enumerate(entry):
            if type(value) is bool:
                list_copy[i][j] = bool_to_string(value)
    return list_copy
