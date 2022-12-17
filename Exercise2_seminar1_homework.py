# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Enter the first coordinate x= '))
y = int(input('Enter the second coordinate y= '))

if x>0 and y>0:
    print(" -> 1 The point is in 1st quarter!")
elif x<0 and y>0:
    print(" -> 2 The point is in 2nd quarter!")
elif x<0 and y<0:
    print(" -> 3 The point is in 3rd quarter")
else:
    print(" -> 4 The point is in 4th quarter!")