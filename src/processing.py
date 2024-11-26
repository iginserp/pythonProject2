def filter_by_state(data: list, state = "EXECUTED") -> list:

    '''Функция фильтрации списка словарей по значению ключа state'''

    filtered_data = []
    for dictionary in data:
        if dictionary["state"] == state:
            filtered_data.append(dictionary)
    return filtered_data

def sort_by_date(data: list, reverse=True) -> list:

    '''Функция фильтрации списка словарей по значению ключа state'''

    sorted_list = sorted(data, key=lambda x: x['date'], reverse=True)
    return sorted_list
