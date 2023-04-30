from typing import List

from aiogram.types import Message, CallbackQuery

from data.config import CHANNELS
from loader import bot


async def check_sub_channels(message):
    for channel in CHANNELS:
        check = await bot.get_chat_member(chat_id='-100' + str(channel[1]), user_id=message.from_user.id)
        if check.status == 'left':
            return False

    return True





# from data.config import CHANNELS
# from aiogram import Bot
# from typing import Union
# async def check_sub_channels(chat_id: Union[int, str], user_id):
#     bot = Bot.get_current()
#     chat_member = await bot.get_chat_member(chat_id=chat_id,user_id=user_id)
#     if chat_member['status'] == 'left':
#         return False
#     return True
