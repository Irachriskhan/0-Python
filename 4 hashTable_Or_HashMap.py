# hashTable or hashMap is a data strucure that maps keys to its value pairs
# chaque element a son image
# 2:40:00

print('Use of dictionary to hash elements')
print('  1-------- Types of decalaring a dictionary')
print()

# By using curly braces
myDict = {'Dave': '001', 'Khan': '002', 'Chris': '003'}
print('Using curly braces: ', myDict)
print()

# By using dict() function
newDict = dict(Dave='001', Khan='002', Chris='003')
print('By using dict() function: ', newDict)
print()

# Nested dictionnary is dictionnary that lie within other dictionnaries
print('  2-------------] Nested dictionnary')
print()
empDetails = {'Employees': {'Dave': {'ID': '001', 'Salary': '2000', 'Designation': 'Team Leader'},
                            'Khan': {'ID': '002', 'Salary': '1000', 'Designation': 'Team Member'}}}
print(empDetails)
print()

print('  3------------ Accessing values on hashtable')  # 2:46:00
print()
print(myDict)
print(myDict['Dave'])  # return the value of x
print(myDict.keys())  # return keys only
print(myDict.values())  # return valies only
print()

print('List of keys by using for loop')
for x in myDict:
    print(x)
print()

print('List of values by using for loop')
for x in myDict.values():
    print(x)
print()

print('List of keys and their values')
for x, y in myDict.items():
    print(x, y)
print()

print('  4----------]Updating')
myDict['Dave'] = '004'
myDict['Roros'] = '003'
print(myDict)
print()

print('  5-----------Deleting')
print(myDict)
print(myDict.pop('Dave'))
print(myDict.items())
del myDict['Chris']
print(myDict)

# import pandas as pd

# df = pd.DataFrame(empDetails['Employees'])
# print(df)
