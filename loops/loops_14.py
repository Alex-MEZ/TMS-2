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
    sr_bal = (uchenik['physics'] + uchenik['informatics'] + uchenik['history']) / 3
    uchenik['sr_bal'] = sr_bal

for uchenik in pupils:
    if uchenik['sr_bal'] > 6:
        print(uchenik['firstname'], '=', uchenik['sr_bal'])

# for uchenik in pupils:
#     sr_bal = (uchenik['physics'] + uchenik['informatics'] + uchenik['history']) / 3
#     uchenik['sr_bal'] = sr_bal
#     if uchenik['sr_bal'] > 4:
#         print(uchenik)
