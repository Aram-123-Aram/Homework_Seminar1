'''
Напишите программу, которая принимает на вход координаты двух точек и находит 
расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''
#variant 1:

print('Enter the coordinates of A:')
Ax = int(input('Enter the Ax= '))
Ay = int(input('Enter the Ay= '))
print('Enter the coordinates of B:')
Bx = int(input('Enter the Bx= '))
By = int(input('Enter the By= '))

import math
dist = round(math.sqrt((Bx-Ax)**2+(By-Ay)**2),2)
print(f'A {Ax,Ay}; B {Bx,By} -> {dist}')
'''
#variant 2:
list1 = [3, 6]
list2 = [2, 1]
import math
dist = round(math.sqrt((list2[0]-list1[0])**2+(list2[1]-list1[1])**2),2)
print(f'A {list1}; B {list2} -> {dist}')
'''
