# Python has functions for creating, reading, updating, and deleting files.
myFile = open('myfile.txt','w')

print ('Name:', myFile.name)
print ('Is Closed:', myFile.closed)
print ('opening mode:', myFile.mode)


myFile.write('I love you, god!')
myFile.write('I am so fortune, I can feel your love and your blessing! I am not a perfect person.')
myFile.write('I have a lot of wicknesses but I am trying to improve myself, so God ')
myFile.write('Please bless me with decipline,determination and intelligent, so i can become a great software developer! thanks god so much!')
myFile.close()
myFile = open('myfile.txt','a')
myFile.write('I love you, god! ')
myFile.write('Thanks for blessing my families!')
myFile.write('Please bless me with decipline,determination and intelligent, so i can become a great software developer! thanks god so much!')
myFile.close()




myFile = open('myfile.txt','r+')
text = myFile.read(1000)

print(text)