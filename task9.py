""" Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y). """

quarter = int(input("Input quarter: "))

if quarter < 1 or quarter > 4:
    print("Error")
elif quarter == 1:
    print("x = (0; infinity), y = (0; infinity)")
elif quarter == 2:
    print("x = (-infinity; 0), y = (0; infinity)")
elif quarter == 3:
    print("x = (-infinity; 0), y = (-infinity; 0)")
else:
    print("x = (0; infinity), y = (-infinity; 0)")
