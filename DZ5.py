# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве

x1 = float(input('Введите координату Х точки 1: '))
y1 = float(input('Введите координату Y точки 1: '))
x2 = float(input('Введите координату Х точки 2: '))
y2 = float(input('Введите координату Y точки 2: '))

Distance = (((x2-x1)**2)+((y2-y1)**2))**0.5
print(f'A ({x1},{y1}) ; B ({x2}, {y2}) = {Distance}') 