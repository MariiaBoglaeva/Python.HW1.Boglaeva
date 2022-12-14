# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

coordinate_quarter= int( input ('Введите номер четверти: '))

match coordinate_quarter:
    case (1):
        print ("X>0 и Y>0")
    case (2):
        print ("X<0 и Y>0")
    case (3):
        print ("X<0 и Y<0")
    case (4):
        print ("X>0 и Y<0")
    case _:
        print ("некорректный номер четверти")