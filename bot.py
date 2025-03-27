from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

TOKEN = os.getenv("TOKEN")  # Токен бота (Railway)
ADMIN_ID = int(os.getenv("ADMIN_ID"))  # Твой Telegram ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("🎵 Заказать бит", callback_data="order")
    keyboard.add(button)
    await message.answer("🔥 Привет! Хочешь заказать бит? Жми на кнопку!", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == "order")
async def process_order(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    user_info = f"🚀 Новый заказ!\n👤 {user.full_name} (@{user.username})\n🆔 ID: {user.id}"
    
    # Отправляем тебе уведомление
    await bot.send_message(ADMIN_ID, user_info)
    
    # Ответ пользователю
    await bot.send_message(user.id, "Спасибо за заказ! 🎶 Владелец скоро свяжется с тобой.")

executor.start_polling(dp, skip_updates=True)
