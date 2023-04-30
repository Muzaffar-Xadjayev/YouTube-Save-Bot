from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def help_user(message: types.Message):
    msg = f"Bot Tomonidan foydalanuvchiga yordam ko'rsatish bo'limi\n" \
          f"Buyruqlar:\n/start — Botni ishga tushirish\n" \
          f"/help — Yordam Ko'rsatish va Bot ishlash tartibi\n\n" \
          f"<b>Botni ishlash tartibi</b>\n\n" \
          f"You Tube Dasturidan biror videoni linkini botga tashlang bot sizga faly tariqasida qaytaradi. " \


    await message.reply(msg)

