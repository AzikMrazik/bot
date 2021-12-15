import logging
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="5097465180:AAFezAkYbiVyBPwL1ujdcYG2PuJh8iYYpzs")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="test1")
async def c1(message: types.Message):
    await message.reply("Test 1")

async def c2(message: types.Message):
    await message.reply("😘es三t 2")

dp.register_message_handler(c2, commands="test2")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
