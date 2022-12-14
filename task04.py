# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

X_cord= []
Y_cord=[]
for i in range(2):
    coordinate_X = int (input(f"Введите X {i+1} точки: "))
    X_cord.append(coordinate_X)
    coordinate_Y= int (input(f"Введите Y {i+1} точки: "))
    Y_cord.append(coordinate_Y)

distance = ((X_cord[1]-X_cord[0])**2+(Y_cord[1]-Y_cord[0])**2)**0.5
# Вывод как в примере (то есть без округления):
dist = str (round(distance,3))
print(f"({X_cord[0]}, {Y_cord[0]}); ({X_cord[1]}, {Y_cord[1]})=> {dist[:len(dist)-1]}")

# Вывод с округлением:
# print(f"({X_cord[0]}, {Y_cord[0]}); ({X_cord[1]}, {Y_cord[1]})=> {round(distance,2)}")