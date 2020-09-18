'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

with open('eng.txt', encoding='utf-8') as f:
    lines = f.readlines()


with open('rus.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        f.write(line)

