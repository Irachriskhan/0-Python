#Specialized collection datatypes
print('Specialized collection datatypes')
print('')

#................namedtuple
#each value is assigned to a name to facilitate the access the valie inside a tuple instead of indexing

print('1--------------- namedtuple')
print('')
from collections import namedtuple
a = namedtuple('courses', 'name, technology, exam')
s = a('data science', 'python', 'monday')
print(s)
print('')
#imprement a tuple using a list
s = a._make(['artificial intelligence', 'python', 'monday'])
print(s)
print('')

#2..................deque
#dueque is used for perfoming insertiom and deletion easily

print('2-------------- deque')
print('')
from collections import deque
a = ['e', 'd', 'u', 'r', 'e', 'k', 'a']
d = deque(a)
print(d)
#add new value or append the deque
d.append('python')
print(d)
d.pop()#delete the last value
print(d)
d.appendleft('python')#add new value at left
print(d)
d.popleft()#delete a value at left
print(d)
print('')

#chainmap
#it is a dictionary like class for creating a single view of multiple mappings

print('3-------------- Chainmap')
print('')
from collections import ChainMap
a = {1 : 'edureka', 2 : 'python'}#diction 1
b = {3 : 'ML', 4 : 'AI'}#dictionnary 2
a1 = ChainMap(a, b)
print(a1)
print('')

#counter
#it is a dictionnary subclass for counting hashable objects... 2:05:00
#hadhable=repetition

print('4-------- counter')
print('')
from collections import Counter
a = [1, 1, 2, 3, 2, 2, 4, 5, 4, 3, 5, 4, 6, 2, 2]
c = Counter(a)#count repetead values from a
print(c)

print(list(c.elements()))#list values by order by ascending

print(c.most_common())#group values and their repeat frequency

sub = {2:1 , 6:1}#decrease 1 time from values 2  and 6
c.subtract(sub)
print(c.most_common())
print('')

#OrderedDict
#it is a dictionnary subclass which remember the order in which the entries done 2:08:00

print('5------------- OrderedDict')
print('')
from collections import OrderedDict
d = OrderedDict()
d[1] = 'e'
d[2] = 'd'
d[3] = 'u'
d[4] = 'r'
d[5] = 'e'
d[6] = 'k'
d[7] = 'a'
print(d)

print(d.keys())

print(d.items())

d[1] = 'p'
print(d)
print('')

#defaultdict
#it is a dictionary subclass which calls a factory funtion to supply missing values 2:12:00

print('6------------- defaultdict')
print('')
from collections import defaultdict
d = defaultdict(int)
d[1] = 'python'
d[2] = 'edureka'
print(d)
print(d[3])#output: 0 bcs d[3] is undefined

#UserDict
#it is a wrapper around dictionnary objects for easier dictionnary sub-classing

#UserList
#it is a wrapper around list objects for easier list sub-classing

#UserString
#it is a wrapper around string objects for easier string sub-classing
