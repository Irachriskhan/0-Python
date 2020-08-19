# Operators 2:56:00
print("Arthimetic operators: -, +, /, * , **, %")
a = 9
b = 2
c = a + b
d = a // b  # it print nombres entiers
e = a ** b  # exponents
f = a % b  # modulo for reminder
print(d)
print(e)
print(f)
print()
# Assignment operator
print('Assignment operator +=, -=, /=, -=, **=')
x = 5
x += 5
print(x)
x = 5
x **= 5
print(x)
x = 5
print()

# comparison operator
print('Comparison operator <, >, >=, <=, !=, ==')
print()

print('Logical operator and, or,  not')
x = 4
y = 5
if x == 5:
    print('Ego ', x, 'na ', y, 'birangana')
else:
    print(x, 'na ', y, 'ntibingana')

print('sample: x<5 and x>10,  x<5 or x>10,  not(x<5 and x>10)')
print()

print('identity operators')
print('Identity operators are used to compare objects')
x =4
y = 4
print(x is y)
print(x is not y)
print()

print('Membership operators: in, not in')
print('They are used to check if a sequence is present in an object')
list1 = [1, 2, 3, 4, 5]
print(list1)
print(1 in list1)
print()

print('Bitwise operators')
print('They are used to compare binary numbers!')
print('they are: Bitwise AND, Bitwise OR, Bitwise XOR, Bitwise NOT, Left Shift, Right Shift')
print(10 & 12)  # 10 = 1010. 12 = 1100 then we get 1000
print(10 | 12)  #
print(10 >> 2)  #
print(10 << 2)  #
print('& , AND: set each bit to 1 if both bits are 1')
print('| , OR: set each bit to 1 if one of the bits is 1')
print('^ , XOR: set each bit to 1 if both bits arte 1')
print('~ , NOT: Invert all bits arte 1')
print('<< , Left Shift: shift left by pushing in zeroes from the right and then let the leftmost bits fell of ')
print('>> , Right Shift: shift right by pushing copies of the leftmost bit in from the left, and let the rightmost '
      'bit fall off ')

