import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Пример использования
clear()
a,b,c,d = int(input()), int(input()), int(input()), int(input())
print((a+b+c+d)*3)
