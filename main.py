import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот 'Дети Света' 🌞")

@bot.message_handler(commands=['post'])
def post(message):
    bot.send_message(message.chat.id, "✨ Здесь будет генерация поста в стиле Солнышка.")

@bot.message_handler(commands=['search'])
def search(message):
    bot.send_message(message.chat.id, "🔍 Функция поиска скоро будет доступна.")

bot.polling()
