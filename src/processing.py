def filter_by_state(data: list, state = "EXECUTED") -> list:

    '''Функция фильтрации списка словарей по значению ключа state'''

    filtered_data = []
    for dictionary in data:
        if dictionary["state"] == state:
            filtered_data.append(dictionary)
    return filtered_data

def sort_by_date(list_dict: list, direction: bool = True) -> list:

    """Функция сортирует словари по дате"""

    sorted_list_by_date = sorted(list_dict, key=lambda x: x["date"], reverse = direction)
    return sorted_list_by_date
