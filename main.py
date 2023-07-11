import subprocess
import os
from pytube import YouTube
from config import TOKEN
from aiogram import Bot, Dispatcher, executor


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message):
    if message.text == '/start':
        await message.answer('Привет! Отправь мне ссылку на Ютуб-видео и я конвертирую его в mp3 файл')


@dp.message_handler(content_types=['text'])
async def convert_handler(message):
    link = message.text.strip()
    yt = YouTube(link)

    stream = yt.streams.get_audio_only()
    input_file = stream.download()

    output_file = input_file.replace('.mp4', '.mp3')
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_file,
        '-vn',
        '-acodec', 'libmp3lame',
        '-ab', '320k',
        '-ar', '44100',
        '-y',
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        with open(output_file, 'rb') as music:
            await bot.send_audio(chat_id=message.chat.id, audio=music)
    except subprocess.CalledProcessError:
        await message.answer('Произошла ошибка')

    os.remove(input_file)
    os.remove(output_file)


executor.start_polling(dp)
