from aiogram import F, types, Router
# from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter
from kbds.reply import get_keyboard

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "Рождён, чтобы ебашить!",
        reply_markup=get_keyboard(
            "Меню",
            "Про бота",
            "Варианты оплаты",
            "Варианты доставки",
            placeholder="Что вас интересует?",
            sizes=(2,)
        ))


@user_private_router.message(or_f(Command('menu'),
                             F.text.lower() == 'меню'))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню, получай: ")


@user_private_router.message(or_f(Command("about"),
                             F.text.lower() == 'про бота'))
async def about_cmd(message: types.Message):
    await message.answer("Что может бот: ")


@user_private_router.message(or_f(Command("payment"),
                                  F.text.lower() == "варианты оплаты"))
async def payment_cmd(message: types.Message):
    text = as_marked_section(
        Bold("Варианты оплаты:"),
        "Картой в боте",
        "При получении карта/кеш",
        "В заведении",
        marker="✅ ",
    )
    await message.answer(text.as_html())


@user_private_router.message(or_f(Command("shipping"),
                                  F.text.lower().contains("доставк"),
                                  F.text.lower() == "варианты доставки"))
async def menu_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold("Варианты доставки/заказа:"),
            "Курьер",
            "Самовынос (сейчас прибегу заберу)",
            "Покушаю у Вас (сейчас прибегу)",
            marker="✅ ",
        ),
        as_marked_section(
            Bold("Нельзя:"),
            "Почта",
            "Голуби",
            marker="❌ "
        ),
        sep="\n----------------------\n",
    )
    await message.answer(text.as_html())


# @user_private_router.message(F.contact)
# async def get_contact(message: types.Message):
#     await message.answer(f"Номер получен")
#     await message.answer(str(message.contact))


# @user_private_router.message(F.location)
# async def get_location(message: types.Message):
#     await message.answer(f"Локация получена")
#     await message.answer(str(message.location))
