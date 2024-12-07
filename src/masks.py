import os
from typing import Any

from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger("masks", file_path_1)

def get_mask_card_number(card: str) -> str:

    '''Функция маскировки номера карты'''

    return card[0:4] + " " + card[4:6] + "** **** " + card[-4:]


def get_mask_account(account: str) -> str:
    '''Функция маскировки номера счета'''
    return "**" + account[-4:]
