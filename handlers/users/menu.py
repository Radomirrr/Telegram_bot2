from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardButton
from keyboards.default.menu import menu, menu_1, menu_2, keyboard_site
from aiogram.dispatcher.filters import Command, Text
import webbrowser

global summa
global big_mak
global big_tasty
global potato_fries
global village_potato
summa = 0
big_mak = 0
big_tasty = 0
potato_fries = 0
village_potato = 0

@dp.message_handler(Command("menu"))
async def show_meny(message: Message):
    await message.answer("Подождите...")
    await message.answer("Выберите товар из меню ниже)",
                         reply_markup=menu)
    

@dp.message_handler(text=("Добавить блюдо 🍔"))
async def show_menu_add(message: Message):
    await message.answer("Подождите...", reply_markup=ReplyKeyboardRemove())
    await message.answer("Выберите блюдо ниже:", reply_markup=menu_1)

@dp.message_handler(text="Биг Мак (145) 🍔")
async def get_bigmak(message: Message):
    global summa
    global big_mak
    await message.answer("В корзину добавлен Биг Мак!. +145")
    summa += 145
    big_mak += 1
    return big_mak, summa

@dp.message_handler(text="Биг Тейсти (249) 🍔")
async def get_bigtasty(message: Message):
    global summa
    global big_tasty
    await message.answer("В корзину добавлен Биг Тейсти!. +249")
    summa += 249
    big_tasty += 1
    return big_tasty, summa

@dp.message_handler(text="Картофель Фри (81) 🍟")
async def get_potatofree(message: Message):
    global summa
    global potato_fries
    await message.answer("В корзину добавлен Картофель Фри!. +81")
    summa += 81
    potato_fries += 1
    return potato_fries, summa

@dp.message_handler(text="Картофель по Деревенски (93) 🥔")
async def get_potatovillage(message: Message):
    global summa
    global village_potato
    await message.answer("В корзину добавлена картошка по деревенски!. +93")
    summa += 93
    village_potato += 1
    return summa, village_potato

@dp.message_handler(text="Назад 🔙")
async def back_to_menu(message: Message):
    await message.answer("Возвращаем вас...", reply_markup=menu)
    await message.answer("Вы снова в главном меню!")

@dp.message_handler(text="Сайт заказа 🍱")
async def site_go(message: Message):
    await message.answer("Нажмите на кнопку, чтобы открыть сайт", reply_markup=keyboard_site)
@dp.message_handler(text="Удалить блюдо ❌")
async def delete_food(message: Message):
    await message.answer("Подождите...", reply_markup=menu_2)
    await message.answer("Выберите ниже блюдо: ")

@dp.message_handler(text="Биг мак ❌")
async def delete_bigmak(message:Message):
    global big_mak
    global summa
    if big_mak > 0:
        await message.answer("Биг Мак удален. -145")
        summa -= 145
        big_mak -= 1
        return big_mak, summa

@dp.message_handler(text="Биг тейсти ❌")
async def delete_bigtasty(message:Message):
    global big_tasty
    global summa
    if big_tasty > 0:
        await message.answer("Биг Тейсти удален. -249")
        summa -= 249
        big_tasty -= 1
        return big_tasty, summa

@dp.message_handler(text="Картофель Фри ❌")
async def delete_fries(message:Message):
    global potato_fries
    global summa
    if potato_fries > 0:
        await message.answer("Картофель Фри удален. -81")
        summa -= 81
        potato_fries -= 1
        return big_tasty, summa

@dp.message_handler(text="Картофель по Деревенски ❌")
async def delete_village(message:Message):
    global village_potato
    global summa
    if village_potato > 0:
        await message.answer("Картофель по Деревенски удален. -93")
        summa -= 93
        village_potato -= 1
        return big_tasty, summa

#@dp.message_handler(text="Сайт заказа 🍱")
#async def go_to_site(message: Message):
    #await message.answer("Открываем сайт для заказа...", reply_markup=keyboard_site)
    #url_delivery = "https://www.delivery-club.ru/srv/Mcdonalds_kzn"
    #webbrowser.open(url_delivery)

@dp.message_handler(text="Сумма заказа 🎫")
async def get_summa(message: Message):
    await message.answer_photo("http://sc-globalcity.ru/sites/default/files/styles/wide_m/public/images/special_offer/vse_chto_vy_lyubite_za.jpg?itok=wpTh3WsT")
    await message.answer(f"Список товаров: \n Биг Мак: {big_mak}x \n Биг Тейсти: {big_tasty} \n Картофель Фри: {potato_fries}x \n Картофель по деревенски: {village_potato}x \n Вообщем у вас выходит: {summa}")