#  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 1 2 3 4 5 6 
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36 

from os import system
def make_operation_table(f, num_rows, num_columns):
    return [[f(x+1 , y+1) for x in range (num_columns)] for y in range (num_rows)]

def print_operation_table(table):
    for i in table:
        for j in i:
            print ('{:^5}'.format(j), end = ' ')
        print()

       
operations = {'+': lambda x, y: x+y,
              '-': lambda x, y: y - x,
              '*': lambda x, y: x*y,
              '/': lambda x, y: round((x/y), 2)}

system('cls')
num_rows = int(input('Введите 1 элемент = '))
num_columns = int(input('Введите 2 элемент = '))

operation = input('Введите операцию: +, -, *, или / ')

print_operation_table(make_operation_table(operations[operation], num_rows, num_columns))



