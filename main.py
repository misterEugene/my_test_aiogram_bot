from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Корзина').add('Контакты')


main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Контакты').add('Админ-панель')


admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Сделать рассылку')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAOfZPw7eHgV7u_5J42anIQzzwyfUm0AAjoUAAKH28lLt4S2aCX5a1QwBA')
    await message.answer(f'{message.from_user.first_name} {message.from_user.last_name}, добро пожаловать в магазин кроссовок!', reply_markup=main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались ка администратор!', reply_markup=main_admin)


@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')


@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer(f'Каталог пуст!')


@dp.message_handler(text='Корзина')
async def cart(message: types.Message):
    await message.answer(f'Корзина пуста!')



@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
    await message.answer(f'Покупать товар у него: @mesudoteac')


@dp.message_handler(text='Админ-панель')
async def cart(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы вошли в админ-панель', reply_markup=admin_panel)
    else:
        await message.reply('Я тебя не понимаю.')


# @dp.message_handler(commands=['end'])
# async def cmd_start(message: types.Message):
#     await message.answer_sticker('CAACAgIAAxkBAAO5ZPw_fRNOvNNiN-Vqnc47810oKXgAAhgUAAJ5dMlLNWs0AYQTWHowBA')
#     await message.answer(f'Досвидания, {message.from_user.first_name} {message.from_user.last_name}')


# @dp.message_handler(content_types=['sticker'])
# async def check_sticker(message: types.Message):
#     await message.answer(message.sticker.file_id)
#     await bot.send_message(message.from_user.id, message.chat.id)


# @dp.message_handler(content_types=['document', 'photo'])
# async def forward_message(message: types.Message):
#     await bot.forward_message(os.getenv('GROUP_ID') , message.from_user.id, message.message_id)


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

