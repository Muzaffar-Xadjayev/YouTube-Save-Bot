import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import sqlite3

from aiogram.types import CallbackQuery

from data.config import ADMINS, CHANNELS
from keyboards.inline.subs import show_channels
from loader import dp, db, bot
from utils.misc.subs import check_sub_channels


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # ADD USER IN DB
    # is_subs = await check_sub_channels(message)
    # if is_subs:
    try:
        await db.add_user(
            telegram_id=message.from_user.id,
            full_name=name,
            username=message.from_user.username
        )


        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"Assalomu alaykum, {message.from_user.full_name}!\n<b>You Tube Save Botga</b> xush kelibsiz!\nMenga link yuboring men sizga fayl ko'rinishida qaytaraman.")
        count = await db.select_all_user()
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {len(count)} ta foydalanuvchi bor."
        for user in ADMINS:
            await bot.send_message(chat_id=user, text=msg)
    except asyncpg.exceptions.UniqueViolationError:
        await message.answer(f"Hurmatli Foydalanuvchi Siz Botga a'zo bo'lgansiz. Bemalol foydalanishingiz mumkin.")
    # else:
    #     btn = await show_channels()
    #     context = f"Assalomu alaykum. Hurmatli <b>{message.from_user.full_name}</b> Botdan foydalanishdan avval quyidagi kanallarga obuna bo'ling!"
    #     await message.answer(context, reply_markup=btn)

# @dp.callback_query_handler(text='sub_channel_done')
# async def check_kanal(call: CallbackQuery):
#     async def is_subs(message):
#         for channel in CHANNELS:
#             check = await bot.get_chat_member(chat_id='-100' + str(channel[1]), user_id=message.id)
#             if check.status == 'left':
#                 return False
#
#         return True
#     che_subs = await is_subs(call["from"])
#     if che_subs:
#         await call.message.delete()
#         try:
#             await db.add_user(
#                 telegram_id=call.from_user.id,
#                 full_name=call.from_user.full_name,
#                 username=call.from_user.username
#             )
#             await call.message.answer(
#                 f"Assalomu alaykum, {call.from_user.full_name}!\n<b>YouTube Save Bot</b>iga xush kelibsiz!")
#             count = await db.select_all_user()
#             msg = f"{call.from_user.full_name} bazaga qo'shildi.\nBazada {len(count)} ta foydalanuvchi bor."
#             try:
#                 for user in ADMINS:
#                     await bot.send_message(user, msg)
#             except:
#                 pass
#         except asyncpg.exceptions.UniqueViolationError:
#             await call.message.answer(
#                 f"Hurmatli Foydalanuvchi siz Bot ga a'zo bo'lgansiz bemalol foydalanishingiz mumkin.")
#     else:
#         await call.answer(text="Berilgan kanallarga obuna bo'ling !", show_alert=True)