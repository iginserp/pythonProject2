def mask_account_card (account_card: str) -> str:

    '''Функция маскировки номера карты'''

    from masks import get_mask_account, get_mask_card_number
    mask = ''
    card_number = ''
    account_number = ''
    if 'Visa' or 'Maestro' in account_card:
        card_number = account_card[-15:0]
        mask = get_mask_card_number(card_number)
    elif 'Счет' in account_card:
        account_number = account_card[-19:0]
        mask = get_mask_account(account_number)
    else:
        return 'неверный формат данных'
    return mask

def get_date (raw_date: str) -> str:

    '''Функция преобразования формата даты'''

    return f"{raw_date[8:10]}.{raw_date[5:7]}.{raw_date[0:4]}"