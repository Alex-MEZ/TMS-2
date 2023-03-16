# Создать список учеников подобной структуры.
# Определить средний балл каждого студента по всем предметам,
# и вывести сведения о студентах, средний балл которых больше 4.
import random

pupils = [
    {
        'firstname': 'Masha',
        'group': 42,
        'physics': random.randint(1, 10),
        'informatics': random.randint(1, 10),
        'history': random.randint(1, 10),
    }, {
        'firstname': 'Igor',
        'group': 42,
        'physics': random.randint(1, 10),
        'informatics': random.randint(1, 10),
        'history': random.randint(1, 10),
    }, {
        'firstname': 'Pasha',
        'group': 42,
        'physics': random.randint(1, 10),
        'informatics': random.randint(1, 10),
        'history': random.randint(1, 10),
    }, {
        'firstname': 'Sasha',
        'group': 42,
        'physics': random.randint(1, 10),
        'informatics': random.randint(1, 10),
        'history': random.randint(1, 10),
    },
]

for uchenik in pupils:
    bal = uchenik['physics'] + uchenik['informatics'] + uchenik['history']
    sr_bal = bal / 3
    uchenik['sr_bal'] = sr_bal

for uchenik in pupils:
    if uchenik['sr_bal'] > 4:
        print(uchenik['firstname'], '=', uchenik['sr_bal'])



