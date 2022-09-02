""" Напишите программу, которая принимает на вход цифру, обозначающую 
день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет """

dayOfWeek = int(input("Insert day of week: "))
if dayOfWeek < 1 or dayOfWeek > 7:
    print("Error")
elif dayOfWeek < 6:
    print("No")
else:
    print("Yes")
