import random
import logging
from datetime import datetime

# Настройка логгирования
logging.basicConfig(filename='game_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Функция для запуска игры
def start_game():
    logging.info('Игра начинается')
    try:
        N = int(input("Введите число N (верхнюю границу диапазона): "))
        k = int(input("Введите число k (количество попыток): "))
        logging.info(f'Пользователь ввел числа N={N} и k={k}')
        if N <= 0 or k <= 0:
            print("Числа N и k должны быть натуральными!")
            logging.warning('Введены некорректные числа N и k')
            return
        secret_number = random.randint(1, N)
        logging.info(f'Загаданное число: {secret_number}')
        make_guess(N, k, secret_number)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите натуральные числа.")
        logging.warning('Введены некорректные данные')

# Функция для попытки угадать число
def make_guess(N, k, secret_number):
    for i in range(k):
        guess = int(input("Попробуйте угадать число: "))
        logging.info(f'Попытка угадать число: {guess}')
        if guess == secret_number:
            print("Поздравляем, вы угадали!")
            logging.info('Игрок угадал число')
            return
        elif guess < secret_number:
            print("Загаданное число больше")
            logging.info('Загаданное число больше')
        else:
            print("Загаданное число меньше")
            logging.info('Загаданное число меньше')
    print(f"Попытки закончились. Загаданное число было: {secret_number}")
    logging.info('Игрок закончил попытки, загаданное число было сообщено')

start_game()

