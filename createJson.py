import datetime 
import json 
dt = datetime.datetime()
with open('Assets/json/todos.json'):
    
    obj = [
        {
            'id': 1,
            'deadline': dt(2022, 2, 14),
            'title': 'Maths class',
            'description': f'The math class hosts on the {dt(2022, 2, 14)} to educate students in maths',
            'isDone': False
        },
        {
            'id': 2,
            'deadline': dt(2022, 2, 17),
            'title': 'Washing',
            'description': f'Have to wash cloths for sunday mass',
            'isDone': False
        },
        {
            'id': 1,
            'deadline': dt(2022, 3, 14),
            'title': 'Cook',
            'description': f'Might have to coo before going to school',
            'isDone': True
        },
        {
            'id': 1,
            'deadline': dt(2022, 2, 14),
            'title': 'Games ',
            'description': f'have to go sporting this afternoon',
            'isDone': True
        },
        {
            'id': 1,
            'deadline': dt(2022, 2, 14),
            'title': 'Maths class',
            'description': f'The math class hosts on the {dt(2022, 2, 14)} to educate students in maths',
            'isDone': False
        },
    ]