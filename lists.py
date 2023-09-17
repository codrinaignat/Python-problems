fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4)) #find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape') #adds grape to fruits list
print(fruits)

fruits.sort()
print(fruits)

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

a = 1
b = 6
for x in range (a, b+1):
    print(x, end = " ")

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)