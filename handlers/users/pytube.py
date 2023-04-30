import os
import time

from aiogram import types
from http.client import IncompleteRead

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Text
from pytube import YouTube
from io import BytesIO
from keyboards.inline.choose_format import choose_format
from loader import dp, bot, db


@dp.message_handler(Text(startswith='http'))
async def get_audio(message: types.Message, state: FSMContext):
    link = message.text
    buffer = BytesIO()
    yt = YouTube(link)
    user_id = message.from_user.id
    await state.update_data(
        {
            "link": link,
            "buffer": buffer,
            "yt": yt,
            "user_id": user_id
        }
    )
    await bot.send_message(user_id, f"Video Nomi: {yt.title}\n"
                                    f"Kanal: <a href='{yt.channel_url}'>{yt.author}</a>", reply_markup=choose_format)

try:
    @dp.callback_query_handler(text="video")
    async def send_video(call: CallbackQuery, state:FSMContext):
        data = await state.get_data('yt')
        await call.message.delete()
        await call.answer(cache_time=60)
        if int(data['yt'].length) // 60 < 13:
            await call.message.answer(f"Yuklash boshlandi.\nVideoning hajmiga qarab 5-10 daqiqa vaqt olishi mumkin")
            sticker = await call.message.answer_sticker(
                "CAACAgIAAxkBAAEG7MVjovfWbjYanFCN2jxO9Ab3eN37-wACFBIAAto4aUh6lAJQnkvJtSwE")
            try:
                await download_video(data['link'])
            except:
                pass
            with open(f"media/{data['yt'].video_id}.mp4", 'rb') as video:
                await call.message.answer_video(
                    video=video,
                    caption='Bu Video <b><a href="https://t.me/youtube_saver_uz_bot">You Tube Save Bot</a></b> tomonidan yuklandi',
                )
                os.remove(f"media/{data['yt'].video_id}.mp4")
            await sticker.delete()
            await state.finish()

            time.sleep(0.05)
        else:
            await call.message.answer(f"Kechirasiz bu bot katta hajmli fayllarni yukla olmaydi. Uzr!")
except:
    pass


try:
    @dp.callback_query_handler(text='audio')
    async def send_audio(call: CallbackQuery, state: FSMContext):
        data = await state.get_data('yt')
        await call.answer(cache_time=60)
        await call.message.delete()
        text = await call.message.answer(f"Yuklash boshlandi.\nAudioning hajmiga qarab 5-10 daqiqa vaqt olishi mumkin.")
        sticker = await call.message.answer_sticker(
            "CAACAgIAAxkBAAEG7MVjovfWbjYanFCN2jxO9Ab3eN37-wACFBIAAto4aUh6lAJQnkvJtSwE")
        if data['yt'].check_availability() is None:
            audio = data['yt'].streams.get_audio_only()
            audio.stream_to_buffer(data['buffer'])
            data['buffer'].seek(0)
            filename = data['yt'].title
            filename += f"\n <a href='https://t.me/youtube_saver_uz_bot'>You Tube Savers Bot</a> Tomonidan yuklandi"
            await call.message.answer_audio(audio=data['buffer'], caption=filename)
            await text.delete()
            await sticker.delete()
        else:
            await call.message.answer("Xatolik")
except:
    pass




try:
    async def download_video(url):
        stream = YouTube(url).streams.filter(progressive=True, file_extension='mp4')
        stream.last().download("media/", f"{YouTube(url).video_id}.mp4")
except:
    pass