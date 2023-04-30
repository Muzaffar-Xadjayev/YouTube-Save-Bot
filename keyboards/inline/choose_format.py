from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

choose_format = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Video', callback_data="video"),
            InlineKeyboardButton(text='Audio', callback_data="audio")
        ]
    ]
)
cancel = InlineKeyboardMarkup(row_width=1)
btn = InlineKeyboardButton(text="🔙 Bekor qilish",callback_data="cancel_btn")
cancel.add(btn)