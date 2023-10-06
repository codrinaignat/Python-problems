#how to display stuff

print("Hello World")

#how to declare a list
myList = [12, 1, 3, 5, 10, 8, 7]
print(myList)

#how to sort a list
print(sorted(myList))

#how to find out the length of a list  
print(len(myList))

#how to define a function with no arguments
def myFunction():
    print("This is my function")
    print("This is a second string")

#how to call a function
myFunction()

#how to define a function with arguments
def suma(a, b):
    return a+b

print("The sum result is: " + str(suma(2, 10)))

#how to define another function with arguments
def print_something(name, age):
    print("My name is ", name, " and my age is ", age)


print_something("Codrina", 26)

#how to define a function with infinite arguments
def print_people(*people):
    for person in people:
        print("THis person is ", person)

print_people("Codrina", "Robert", "Plush", "Gusy")

def do_math(num1, num2):
    return num1 + num2

math1 = do_math(5, 7)
math2 = do_math(10, 2)

print("The first sum is", math1, "and the second sum is",math2)

#if - elif - else statements
check = "Hamburger"
if check == False:
    print("It is false")
elif check == "Hamburger":
    print("It is a hamburger")
else:
    print("It is actually true")

#loops

numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item)

run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current +=1

import re
string = "'I AM NOT YELLING', she said. Though we knew it to not be true"
print(string)
new = re.sub('[A-Z]', '', string) #this replaces all the capital letters in string with nothing
print(new)
