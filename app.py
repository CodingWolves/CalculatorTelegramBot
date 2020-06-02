import os

from EasyTeleBot import CreateEasyTelegramBot

easy_bot = CreateEasyTelegramBot('config.json', telegram_token=os.environ['TELEGRAM_TOKEN'])

app = easy_bot.flask_app

if __name__ == '__main__':
    print('main function started')
    app.run()
