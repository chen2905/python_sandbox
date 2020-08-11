# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
fruits =('Apples','Oranges','Grapes')





#print(fruits,type(fruits))


#can't the value of tuble
#fruits[1] = 'Banana'

print(fruits[1])
# A Set is a collection which is unordered and unindexed. No duplicate members.


#del tuble

#del fruits

#print(fruits)
#a set is a collection which unorderred and unindexed. no duplicate members

#create set

fruits_set = {'Apples', 'Oranges', 'Mango'}

#print('Apples' in fruits_set)

fruits_set.add('Grape')
fruits_set.add('Grape')
#fruits_set.remove('Grape')

print(fruits_set)
# clear set

fruits_set.clear()

print (fruits_set)