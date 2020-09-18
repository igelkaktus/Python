# encoding='utf-8'
# SyntaxError: Non-UTF-8 code starting with '\xd0' in file D:/DATA/PythonProjects/PythonProjects/Lesson_05/Task_6.py on line 4, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

my_dict = dict()
with open('6.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        splitted_line = line.split()
        subject = splitted_line[0]
        sum_lessons = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
        my_dict[subject[:-1]] = sum_lessons
print(my_dict)
