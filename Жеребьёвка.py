# -*- coding: utf-8 -*-
import random
#Ввод и проверка значения N
while True :
    try:      
        N = int(input('''Введите число бочонков, которое хотите положить в мешок:
(для выхода нажмите 0)\n'''))
    except ValueError: 
        N = 'error'
            
    if N == 'error':
        print('Попробуйте еще раз.')
        continue
    elif N < 0 :
        print('Число число должно быть больше 8')
        continue
    elif N == 0 :   
        break
    bag = []
    choise = ' '
    while choise != 'n':
        try:    
            choise = input('''Если хотите вытянуть бочонок, введите "y"
если нет - "n" ''')
        except ValueError:
            choise = 'error'
        if choise == 'error':
            print('Попробуйте еще раз.')
        elif choise == 'y':
            x = random.randint(1, N)
            if len(bag) == N and x in bag:
                print('В мешке больше нет бочонков.')
                continue   
            elif x not in bag:
                bag.append(x)
                print('Выпавший номер бочонка:', x)
            elif x in bag:
                while x in bag:
                    x = random.randint(1, N)
                bag.append(x)
                print('Выпавший номер бочонка:', x)
        elif choise == 'n':
            break
        
