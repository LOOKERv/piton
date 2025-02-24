import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Пример использования
clear()
a_1, b_1, a_2, b_2 = int(input()), int(input()), int(input()), int(input())
if (a_1 == b_2) or (a_2 == b_1):#точка
    if a_1 == b_2:
        print(a_1)
    else:
        print(a_2)
elif (a_1 == a_2) and (b_1 == b_2): #равны
    print(a_1, b_1)
elif (b_1<a_2) or (b_2>a_1) :
    print('пустое множество') # не пересекаются
#https://stepik.org/lesson/265082/step/11?thread=solutions&unit=246030