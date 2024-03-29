# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением
# дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def func(sp):
    min=sp[0]%1
    max=sp[0]%1
    sp1=[]
    for i in range(0,len(sp)):
        sp1.append(round(sp[i]%1,2))
        if sp1[i]<min and sp1[i]!=0:
            min=sp1[i]
        if sp1[i]>max:
            max=sp1[i]
    return max,min

sp=[1.1, 1.2, 3.1, 5, 10.01]
max,min=func(sp)

print(f'Максимальная дробная часть {max}.\
    \nМинимальная дробная часть {min}.\
    \nРазница между ними {max-min}')