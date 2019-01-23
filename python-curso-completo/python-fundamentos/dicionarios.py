professor = {'nome': 'Robson', 'idade': 42, 'cursos': ['Java', 'Python']}
professor

professor['nome']
professor['idade']
professor['cursos']
professor['cursos'][0]

professor.keys()
professor.values()
professor.items()
professor.get('idade')
professor.get('tags', '[]')

professor['idade'] = 44
professor
professor['cursos'].append('Scala')
professor

professor.pop('idade')
professor

professor.update({'idade': 40, 'Sexo': 'M'})
professor

professor.clear()
professor
