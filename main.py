from functions import *

start_message()
game()
while True:
    response = input('Хотите еще раз сыграть в игру? (да/нет): ')
    if response == 'да':
        game()
        continue
    elif response == 'нет':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
    else:
        print('Некорректный ответ, введите либо "да", либо "нет"')
        continue



