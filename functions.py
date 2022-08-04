import time
import random

def start_message():
    print('Добро пожаловать в числовую угадайку!')
    time.sleep(3)
    print('Цель игры - угадать число')
    time.sleep(3)

def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100

def game():
    count = 0
    random_number = random.randint(1, 101)
    while True:
        user_number = input('Угадайте число: ')
        if is_valid(user_number):
            user_number = int(user_number)
            if user_number < random_number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                count += 1
            elif user_number > random_number:
                print('Ваше число больше загаданного, попробуйте еще разок')
                count += 1
            else:
                print('Вы угадали, поздравляем!')
                print('Число попыток:', count)
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue