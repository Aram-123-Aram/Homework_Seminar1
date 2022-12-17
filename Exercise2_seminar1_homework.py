'''
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого 
выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.
'''
x = None
y = None
z = None
list = [x, y, z]

if not (list[0] or list[1] or list[2]) == (not list[0]) and (not list[1]) and (not list[2]):
    print(True)
else:
    print(False)