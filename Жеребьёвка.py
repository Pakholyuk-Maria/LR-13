# -*- coding: utf-8 -*-
import random
#Ввод и проверка значения N
while True :
    try:      
        N = int(input('''Введите целое число > 0:\n
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
    print('Выпавшие номера бочонков: ')
    bag = []
    while len(bag) != N:
        x = random.randint(1, N)
        if x in bag:
            continue
        elif x not in bag:
            bag.append(x)
            print(x)
