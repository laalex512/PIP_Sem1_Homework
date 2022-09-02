""" Напишите программу для. проверки истинности 
утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. """


resultOfCompare = True

for x in range(2):
    for y in range(2):
        for z in range(2):
            leftPart = not (x or y or z)
            rightPart = not x and not y and not z
            print(f"{leftPart}   =   {rightPart}")
            if leftPart != rightPart:
                resultOfCompare = False

print(resultOfCompare)
