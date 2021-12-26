from django.core.management.base import BaseCommand
import telebot
from telebot import types
from core.models import Client

class Command(BaseCommand):
    help = 'Start Bot'

    def handle(self, *args, **options):
        
        bot = telebot.TeleBot("token")

        @bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            client = Client(tg_id=message.from_user.id)
            client.save()

            _message = 'Спасибо за проявленный интерес! \nЯ пока недоступен, но скоро вернусь с новостями)'
            bot.send_message(message.from_user.id, text = _message)
            bot.send_message(message.from_user.id, text = '🎉')

            bot.send_message(399926757, text = f"Новая регистрация в боте! \nПосмотрим на этот ебальничек! - @{message.from_user.username}")
            bot.send_message(425974638, text = f"Новая регистрация в боте! \nПосмотрим на этот ебальничек! - @{message.from_user.username}")

        bot.polling(none_stop=True, interval=0)