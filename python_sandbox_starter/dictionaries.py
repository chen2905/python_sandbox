# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


#Create dic

person ={
    'first_name':'John',
    'last_name':'Doe',
    'age':30
}

print(person,type(person))

#Use constructor

person2=dict(first_name='Sara',last_name= 'William')

print(person2, type(person2))

#Get vallue

# print(person2['last_name'])
# print(person2.get('last_name'))

# # print(person.keys())
# # print(person.items())

# person3 = person.copy()

# person.pop('age')

# print(person)

# #person.clear()
# print (len(person))

people =[
    {'name':'Martha','age':30},
    {'name':'Kevin','age':25}
]

print(people[1]['name'])