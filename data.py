import telebot
from telebot import types

bot = telebot.TeleBot("5060193439:AAEAmwRBjQKmRslF6-TzEWpFFIVcXRmbkK8")

color = ["Красный", "Розовый", "Фиолетовый", "Чёрный", "Белый", "Серый", "Зелёный", "Лаймовый", "Салатовый"]
counts = [340, 210, 100, 640, 410, 200, 940, 610, 300]

question = [
    ["Ваш цвет из семейства красных?", 100],
    ["Ваш цвет красный или розовый?", 110],
    ["Ваш цвет красный?", 130],
    ["Ваш цвет из семейства монохромных?", 200],
    ["Ваш цвет черный или белый?", 210],
    ["Ваш цвет черный?", 230],
    ["Ваш цвет из семейства зелёных?", 300],
    ["Ваш цвет зелёный или лаймовый?", 310],
    ["Ваш цвет зёленый?", 330],
]

count = 0
true_color = "Бесцветный"