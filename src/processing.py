def filter_by_state(data: list, state = "EXECUTED") -> filtered_data: list

    '''Функция фильтрации списка словарей по значению ключа state'''

    filtered_data = []
    for dictionary in data:
        if dictionary["state"] == state:
            filtered_data.append(dictionary)
    return filtered_data