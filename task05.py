
# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for x in range(2):
    for y in range(2):
        for z in range(2):
            right_side= not (x or y or z)
            left_side= not x and not y and not z
            identity= right_side==left_side
            print (f"x={x}, y={y}, z={z}-> {identity}")
