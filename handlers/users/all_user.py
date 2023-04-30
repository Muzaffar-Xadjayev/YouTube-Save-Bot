from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(commands='count', user_id=ADMINS)
async def all_user(msg: types.Message):
    users = db.count_user()[0]
    text = f"Bazada {users} ta foydalanuvchi bor:\n\n"
    num = 0
    a = ''
    for i in db.select_all_user():
        num+=1
        a += f"<a href='tg://user?id={i[0]}'>{i[1]} [{i[0]}]</a>\n"
    text += a
    await bot.send_message(ADMINS[0], text)
