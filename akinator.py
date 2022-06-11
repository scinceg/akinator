from pip import main
import telebot
from telebot import types
import data
import time


@data.bot.message_handler(commands=["start"])
def welcome(message):

    welcome_str = "Привет, {0.first_name}, я <b>Акинатор</b>!".format(message.from_user,
                                                                      data.bot.get_me())

    simple_keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    color_key = types.KeyboardButton("Загадать цвет")

    simple_keyboard.add(color_key)

    data.bot.send_message(message.chat.id, welcome_str,
                          parse_mode="html", reply_markup=simple_keyboard)


@data.bot.message_handler(commands=["color"])
def answer(message):
    calculate_color(data.count)
    data.count = 0
    data.bot.send_message(message.chat.id, data.true_color, reply_markup=None)


@data.bot.message_handler(content_types=["text"])
def start(message):
    if message.chat.type == "private":
        if message.text == "Загадать цвет":
            game_text = "На данный момент я могу отгадывать один из этих цветов: {}, выбери цвет и нажми 'Поехали!'.".format(
                data.color)

            go_keyboard = types.ReplyKeyboardMarkup(
                resize_keyboard=True, one_time_keyboard=True)
            go_key = types.KeyboardButton("Поехали!")
            go_keyboard.add(go_key)
            data.bot.send_message(message.chat.id, game_text,
                                  parse_mode="html", reply_markup=go_keyboard)

            global number_of_quenstions
            for number_of_quenstions in range(len(data.question)):

                yesno_keyboard = types.ReplyKeyboardMarkup(
                    resize_keyboard=True)
                yes_key = types.KeyboardButton("Да")
                no_key = types.KeyboardButton("Нет")
                stop_key = types.KeyboardButton("Стоп")
                yesno_keyboard.add(yes_key, no_key, stop_key)

                msg = data.bot.send_message(message.chat.id, data.question[number_of_quenstions][0],
                                            reply_markup=yesno_keyboard)
                data.bot.register_next_step_handler(msg, input_answers)
                time.sleep(4)


def input_answers(message):
    if message.text == "Да":
        data.count += data.question[number_of_quenstions][1]
        return data.count
    if message.text == "Стоп":
        main.bot.stop_polling()

def calculate_color(count):
    found = data.counts[0]
    for item in data.counts:
        if abs(item - count) < abs(found - count):
            found = item
    for i in range(len(data.counts)):
        if found == data.counts[i]:
            data.true_color = data.color[i]
            return data.color[i]


data.bot.polling(none_stop=True)
