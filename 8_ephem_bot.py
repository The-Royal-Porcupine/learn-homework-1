"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import setting


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {
    'proxy_url': setting.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': setting.PROXY_USERNAME,
        'password': setting.PROXY_PASSWORD
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def constellation(bot, update):

    planet = update.message.text.split()[1]

    if hasattr(ephem, planet):
        if hasattr(ephem, planet):
            planet = getattr(ephem, planet)()
            planet.compute()
            cons = ephem.constellation(planet)
            update.message.reply_text(cons)
    else:
        text = 'Такой планеты нет, дружок'
        update.message.reply_text(text)


def main():

    mybot = Updater(setting.API_KEY, request_kwargs=PROXY)

    commands = [
        ["start", greet_user],
        ["planet", constellation]
    ]

    dp = mybot.dispatcher
    for command, function in commands:
        dp.add_handler(CommandHandler(command, function))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
