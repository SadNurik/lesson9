import random
print('Игра Камень-Ножницы-Бумага')
print('Введите число: \n 1 - Камень \n 2 - Ножницы \n 3 - Бумага')

igrok = int(input('Введите число от 1 до 3-х: '))
if igrok == 1:
    print('Вы выбрали камень')
elif igrok == 2:
    print('Вы выбрали ножницы')
elif igrok == 3:
    print('Вы выбрали бумагу')
else:
    print('Введите числа от 1 до 3-х!!!')
    exit(0)

comp = random.randint(1, 3)
if comp == 1:
    print('Компьютер выбрал камень')
elif comp == 2:
    print('Компьютер выбрал ножницы')
elif comp == 3:
    print('Компьютер выбрал бумагу')

if igrok == 1 and comp == 1:
    print('ничья')
if igrok == 1 and comp == 2:
    print('Вы победили')
if igrok == 1 and comp == 3:
    print('Вы проиграли')
if igrok == 2 and comp == 1:
    print('Вы проиграли')
if igrok == 2 and comp == 2:
    print('ничья')
if igrok == 2 and comp == 3:
    print('Вы победили')
if igrok == 3 and comp == 1:
    print('Вы выиграли')
if igrok == 3 and comp == 2:
    print('Вы проиграли')
if igrok == 3 and comp == 3:
    print('ничья')