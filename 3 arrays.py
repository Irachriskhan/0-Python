# arrays are data structure which can hold one or more values at a time. it is a collection or ordered series of
# elements of same type. 2:15:00

print('  1----------------------Types of declaring an Arrays in python')
print('')
# an array differ from a list because an array store data of same type and accept multiplication or addition by a number at all elements
# but an element store  data of diffenttypes at time.

# --------------------------------------------

print('Type One: by uding the constructor array ')
# import array
  # a = array.array('i', [1, 2, 3, 4, 5, 6])
# print(a)
# analyse of the code
# a: array name
# array :name of the module
# array: array constructor
# i : type code for integers = type of elements stored in array
# d : is a type code for float numbers
print('')

# --------------------------------------------
print('Type Two: with the alias name arr ')
# import array as arr
# a = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
# print(a)
print('')
# --------------------------------------------
print('Type Threee: by using *')
from array import *

a = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)
print(a[3])  # element at index 3
print(a[-2])  # element at index -2: from right
print(len(a))  # length of an array
print('')

print('Appended array: one value is added')
a.append(10)  # append() add one element ata the end of an array
print(a, 'The value 10 is added at last position')
print('')

print('Extended array: many value are added')
a.extend([11, 12, 13, 14])
print(a, '4 last elements are added')
print('')

print('values inserted in an array')
a.insert(2, 0)  # 2 is an index no, 0 is a value to be inserted
print(a)
print('')

print('  2----------------Deleting elements from an array')
print(a.pop())  # used to delete the last element and display it or return the deleted value
print(a, 'Here, the last value 14 is deleted')
print(a.remove(0))  # used to delete a specified value here it is 0 but does not return it
print(a, 'The value 0 is deleted')
print()
print(a.pop(3))  # it delete the value of index 3
print(a.pop(-2))  ##it delete the value of index -2
print(a, ' two values  4 and 12 are deleted from the previous array')
print()

print('  3----------------Array concatination')
f = array('d', [1.0, 2.3, 4.5, 6.7])
g = array('d', [3.1, 4.3, 9.1, 8.4])
print(f);
print(g)
h = array('d')
h = f + g
print(h, ' Array f and g are concatinated')
print()

print('  4-----------------Slicing an array: search a values from an array')
print(a)
print(a[2:6], 'These are values from index 2 up to 6 excluded')
print(a[2: -2], 'These are values from index 2 up to -2 excluded')
print(a[::-1], 'It inverse the array')
print()

print('  5---------------Looping through Arrays')
print()

# for loop: iterates over the items of an array specified number of times'
print('For loop')
print(a)
print('print All elements of a using for loop ')
for x in a:
    print(x)
print()

print('display specified values of a from index 2 up to -2 excluded')
for x in a[2: -2]:
    print(x)
print()
# while loop: iterates over the elements until a certain condition is met
print('While loop')
print(a)
temp = 0
while temp < a[4]:  # verify until value at index 4
    print(a[temp])
    temp += 1  # equals temp=temp+1
print()

print(a)
print('Display the array by using len() function')
tem = 0
while tem < len(a):
    print(a[tem])
    tem += 1
