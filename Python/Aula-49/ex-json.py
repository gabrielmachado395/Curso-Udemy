import json

d1 = {
    'Pessoa 1': {
        'nome': 'Pedro',
        'idade': 18,
    },
    'Pessoa 2': {
        'nome': 'Luiz',
        'idade': 28,
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

