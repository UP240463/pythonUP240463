# dia 9

#1.Verificar y obtener el skill intermedio, si existe la clave skills en el diccionario:

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print(f"La habilidad intermedia es: {middle_skill}")

#2.Verificar si Python está en las habilidades:

if 'skills' in person and 'Python' in person['skills']:
    print("La persona tiene la habilidad de Python.")
else:
    print("La persona no tiene la habilidad de Python.")

#3.Verificar el rol según las habilidades:

if 'skills' in person:
    skills = person['skills']
    
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('Unknown title')

#4.Verificar si está casado y vive en Finlandia:

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")