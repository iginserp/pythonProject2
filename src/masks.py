def get_mask_card_number(card: str) -> str:

    '''Функция маскировки номера карты'''

    return card[0:3] + " " + card[4:5] + "** **** " + card[-4:]


def get_mask_account(account: str) -> str:
    '''Функция маскировки номера счета'''
    return "**" + account[-4:]
