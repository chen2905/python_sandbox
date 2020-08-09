# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'CHEN GAO'
age = 40

#Concatenate

print('hello, my name is '+ name +' and my age is ' + str(age))


# String Formatting


#Arguments by position
print ('My name is {name} and I am {age}'.format(name=name, age=age))

#F-strings (3.6+)
#print (f'Hello, my name is {name} and I am {age}')
# String Methods
s = 'hello world'
print ('#string method'+s.capitalize())
print ('length:'+ str(len(s)))
print ('replac:'+ s.replace('world','God'))
print ('split:'+str(list(s.split())))
print ('find:'+str(s.find('o')))
print (' is all alphanumberic:'+str(s.isalnum()))
print (' is all isalpha:'+str(s.isalpha()))