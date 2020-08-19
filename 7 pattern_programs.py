#  Pattern programs: Star pyramid, half pyramid, triangle, hourglass, diamond and inverted patterns
#  Pyramid pattern 3:48:54

def pattern(n):  # n identify the number of line in the pattern
    k = 2 * n - 2  # for blank space
    for i in range(0, n):  # loop for rows
        for j in range(0, k):  # loop for columns
            print(end=" ")  # print blank spaces
        k = k - 1
        for j in range(0, i + 1):
            print('* ', end='')
        print('\r')


pattern(8)
print()


# ____________________________________________________________________________________
# Inverse pattern

def pattern(n):  # n identify the number of line in the pattern
    k = 2 * n - 2  # for blank space
    for i in range(n, -1, -1):  # loop for rows
        for j in range(k, 0, -1):  # loop for columns
            print(end=" ")  # print blank spaces
        k = k + 1  # k = k + 1 to display italic triangle
        for j in range(0, i + 1):
            print('* ', end='')
        print('\r')


pattern(8)
print()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print()


#  Right star pattern
def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern(6)
print()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print()


#  Left star pattern
#  time 04:00:00

def pattern(n):
    k = 2 * n - 2
    for i in range(0, n-1):
        for j in range(0, k):
            print(end="")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = -1
    for i in range(n-1, -1, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k = k + 2
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")


pattern(10)
