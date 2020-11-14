from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Добавить блюдо 🍔"),
        KeyboardButton(text="Удалить блюдо ❌")
    ],
    [
        KeyboardButton(text="Сумма заказа 🎫"),
        KeyboardButton(text="Сайт заказа 🍱")       
    ],
  ],
    resize_keyboard=True,
)
menu_1 = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Биг Мак (145) 🍔"),
        KeyboardButton(text="Биг Тейсти (249) 🍔")
    ],
    [
        KeyboardButton(text="Картофель Фри (81) 🍟"),
        KeyboardButton(text="Картофель по Деревенски (93) 🥔")
    ],
    [
        KeyboardButton(text="Назад 🔙")
    ],
    ],
    resize_keyboard=True,
)
menu_2 = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Биг мак ❌"),
        KeyboardButton(text="Биг тейсти ❌")
    ],
    [
        KeyboardButton(text="Картофель Фри ❌"),
        KeyboardButton(text="Картофель по Деревенски ❌")
    ],
    [
        KeyboardButton(text="Назад 🔙")
    ],
    ],
    resize_keyboard=True,
)
keyboard_site = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Сайт заказа 🍱", url="https://www.delivery-club.ru/srv/Mcdonalds_kzn")
        ],
        ]
)
    