#declaration of numbers
#tips of numbers
print('Declaration of Numbers ')
x=3; y=1.5; z=23j
i=9>5; t=7<6
print('x=', x)
print('type of x:', type(x))
print('y=', y)
print('type of y:', type(y))
print('z=', z)
print('type of z:', type(z))
print('i=', i)
print(type(i))
print('t=', t)
print(type(t))
print('')

#manipulate a string
print('Declaration of Strings')
phrase="I love my home country"# a string
print("string length", len(phrase))#check the length
print('index 5:', phrase[5])#check the index no five
print('index 2 to 14:', phrase[2:14])
print("  ")
print('index -14:', phrase[-14])
print('to uppercase:', phrase.upper())#to uppercase
print('to lowercase:', phrase.lower())#to lowercase
print(' ')

#declaration of a list
#list manipulation
#is ordered, changeable and duplicatable

print('manipulate a list')
givenList=[2, 3, 8, 'abana', 'inka', 'impene' ] #declaration of a list
print(givenList)
print('list from index 0 to 4:', givenList[0:4])
givenList[2]='abantu'#update a given index in a list
print('index 2 is updated:', givenList)
givenList.append('abagore')#add another element in a list
print(givenList)
givenList.insert(7, 'inzoya')#add element at specified index
print(givenList)
givenList.reverse()#reverse the list order
print('The reversed givenList:', givenList)
print(' ')

#dictionary manipulation
#can be unorded, changed but entries cannot be duplicated

print('dictionary tips')
courses = {
	1 :  'python',
	2 : 'java',
	'third' : 'Machine Learning',
	4 : 'Artificial Intelligence'
}#declaration of a dictionary

print('the list of courses:', courses)
print('the first course is:', courses[1])
print('the first course is:', courses.get(1))
courses['third'] = 'Javascript'#replace an entry
print('the updated course is:', courses)
courses['five'] = 'Machine Leaning'#add new entry
print('the modified course is:', courses)
print(' ')

#Tuple manipulation
#Tuple are ordered, cannot be changed, entries can be duplicated, support indexing

print('Tuple manipulation')
animals= (1, 2, 2, 3, 'imbwa', 'inka', 'inka', 'intama')
print('animals are:', animals)
print(animals.count(2))
print(animals.count('inka'))#count inka in animals
print(animals[5])#call an index
print(' ')

#set manipulation
#unordered, no duplication of entries
#doesnot support inedexing

print('set manipulation')
mySet = {10, 20, 20, 'indimu', 'inanasi','inanasi'}
print('my set is:', mySet)
#print(mySet[1])
print(' ')

#range manipulation
print('Range manipulation!')
range(10)#declaration of a range
print(range(10))
print('This is a range from 0 to 10:', list( range(11)))
print('')
dig = {1, 2, 3, 4}#dictionary
lis = [5, 6, 7, 8]#list
dl = [dig , lis]
print('dictionary:', dig)
print('list:', dig)
print('dictionary + list =', dl)

