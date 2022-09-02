""" Напишите программу, которая принимает на вход координаты
 точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти 
 плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 """

x = float(input("Insert X: "))
y = float(input("Insert Y: "))

if x > 0 and y > 0:
    print("1st quarter")
elif x < 0 and y > 0:
    print("2nd quarter")
elif x < 0 and y < 0:
    print("3rd quarter")
elif x > 0 and y < 0:
    print("4rd quarter")
else:
    print("Point is at the intersection of the axe(s)")