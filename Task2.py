import random

def list_random():
    work_list = []
    cou = random.randint(10, 25)
    for _ in range(cou):
        r_val = random.randint(-100, 100)
        work_list.append(r_val)
    return work_list

def pos_in_range(work_list, border_list):
    index_list = [i for i in range(len(work_list)) if min(border_list) <= work_list[i] <= max(border_list)]
    return index_list

work_list = list_random()
print('Задайте границы искомого диапазона. \n'
        'Введите два целочисленных значения через пробел:')
input_list = input().split()
border_list = [int(i) for i in input_list]
if border_list[0] != min(border_list):
    border_list.reverse()
print(f'Исходный список:\n{work_list}')
print('К заданному диапазону: {', *border_list, '} принадлежат элементы списка, расположенные на позициях:\n'
      f'{pos_in_range(work_list, border_list)}' )



