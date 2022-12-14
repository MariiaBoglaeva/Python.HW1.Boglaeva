
# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# x= bool (input("Введите значение X: "))
# y= bool (input("Введите значение Y: "))
# z= bool (input("Введите значение Z: "))

for x in range(2):
    for y in range(2):
        for z in range(2):
            right_side= not (x or y or z)
            left_side= not x and not y and not z
            identity= right_side==left_side
if identity:
    print ("Выражение истинно для всех значений предикат")
else:
    print ("Выражение не является истинным для всех значений предикат")
