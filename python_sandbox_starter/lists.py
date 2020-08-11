# A List is a collection which is ordered and changeable. Allows duplicate members.
# create List
numbers = [1, 2, 3, 4, 5]

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# use a constructor
number2 = list((1, 2, 3, 4, 5, 6))

# print(numbers,numbers)

# Get a value

# print(fruits[1])

# Get length
# print(len(fruits))
# Append to list

fruits.append('Mangos')

# remove list
fruits.remove('Grapes')

# inset into position

fruits.insert(2, 'Strawberries')

# remove with pop
fruits.pop(2)
# reverse

fruits.reverse()

fruits.sort()

fruits.sort(reverse=True)

# change value
fruits[0] = 'Banana'

print(fruits)
