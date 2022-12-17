# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_of_week = int(input('Enter the number day of week: ')) 

if day_of_week == 6 or day_of_week == 7:
    print("Ura!!! Today is Weekend! It's time for hiking!")
else:
    print("Today is a working day.I can't go hiking with you")
