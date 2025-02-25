import os
import telebot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Replace 'TELEGRAM_BOT_TOKEN' with the token you received from BotFather
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

SEX_STICKERS = [
    "CAACAgIAAxkBAAKfNme-NZb7--r7PXCbOQ0x516SmyKoAAIVDQACYelqBJQyS8-Po-e4NgQ", 
    "CAACAgIAAxkBAAKfOWe-NaZ7kgzyegQdc52_GwEfsmT3AAIZDQACYelqBBmyIsVLnCsXNgQ",
    "CAACAgIAAxkBAAKfPGe-Nc9ZKhWho9kXKHvUa835aWKdAAJUCAACudaLAqgt9JPmoncWNgQ",
    "CAACAgIAAxkBAAKfP2e-NgGz7uJb_pOwHZB9Cr2rnmcCAAJRFwACWGaYShxhWthlqCRaNgQ", 
    "CAACAgIAAxkBAAKfQme-NoTTSsbTvu4gIOM_WTt9g94gAAI2AANq508XwrzHaPNtLL02BA",
    "CAACAgIAAxkBAAKfRWe-Np73-KvnkX6QPE5ZN4CiYtGeAAI1lwACY4tGDG9cZuUTjkLvNgQ",
    "CAACAgIAAxkBAAKfY2e-O1xrUIJHIz-qFRTiwDpQiBnTAALvFAACjrf5SuP_nqwD9IiiNgQ"
]
NAHUI_STICKERS = [
    "CAACAgIAAxkBAAKfSGe-OlmtNho5g1hfd9vANgQMW8xkAAJXOwACuWuRS7lRMw31qJzKNgQ", 
    "CAACAgIAAxkBAAKfTme-Ons0ncVbpVRF1lZ_x7uFYSv9AAJ-NAACyvThS9U9N1W-wc7yNgQ",
    "CAACAgIAAxkBAAKfYGe-OzAIgRzt0N2uzDfSg-D7-oYEAAKaEwACxThwSHyiN0DnwiKENgQ",
    "CAACAgQAAxkBAAKfVGe-Ot-xco0SNd5f8tJXh7l64WLuAALlCAACBLdoUptLHUJBk0XYNgQ", 
    "CAACAgUAAxkBAAKfbGe-PF-qaVV1te_RU065bSDo4RpGAAK_BQAC_JtpVARCpz2mcvahNgQ",
]
     
        
@bot.message_handler(func=lambda message: message.reply_to_message is not None and ("трахнуть" in message.text.lower() or "трахать" in message.text.lower()))
def check_sex(message):
    user_one = message.from_user
    user_two = message.reply_to_message.from_user
    if user_one and user_two:
        response = f"{user_one.first_name} трахнул(а) {user_two.first_name}"
        bot.send_message(message.chat.id, response)
        bot.send_sticker(message.chat.id, random.choice(SEX_STICKERS))
        
@bot.message_handler(func=lambda message: message.reply_to_message is not None and ("послать" in message.text.lower()))
def check_sex(message):
    user_one = message.from_user
    user_two = message.reply_to_message.from_user
    if user_one and user_two:
        response = f"{user_one.first_name}: {user_two.first_name}, иди нафиг"
        bot.send_message(message.chat.id, response)
        bot.send_sticker(message.chat.id, random.choice(NAHUI_STICKERS))

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
