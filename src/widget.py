from src.masks import get_mask_account, get_mask_card_number

def mask_account_card (account_card: str) -> str:

    '''Функция маскировки номера карты'''

    if 'Visa' in account_card or 'Maestro' in account_card  or 'MasterCard' in account_card:
        card_number = account_card.split()[-1]
        mask = get_mask_card_number(card_number)
    elif 'Счет' in account_card:
        account_number = account_card.split()[-1]
        mask = get_mask_account(account_number)
    else:
        return 'неверный формат данных'
    return " ".join(account_card.split()[:-1]) + " " + mask

print(mask_account_card("Счет 73654108430135874305"))


def get_date (raw_date: str) -> str:

    '''Функция преобразования формата даты'''

    return f"{raw_date[8:10]}.{raw_date[5:7]}.{raw_date[0:4]}"