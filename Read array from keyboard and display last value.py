myList = []
x = int(input("Number of elements: "))
for i in range(0,x):
    elements = int(input())
    myList.append(elements)
print(myList)

lastElement = myList[-1]
print("Last element is: ", lastElement)
