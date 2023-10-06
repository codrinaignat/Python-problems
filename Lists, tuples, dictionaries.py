#Ex1

namesList = ["Codrina", "Victoria", "Robert", "Adrian"]
print(namesList[1])

#Ex2

listOfSports = ["Tennis", "Football", "Cycling", "Curling"]
print(listOfSports)
listOfSports[1] = "Cycling"
print(listOfSports)

#Ex3

listOfNumbers = [1,2,3,4,5,6,7,8,9,10]
print(listOfNumbers)
del listOfNumbers[4]
print(listOfNumbers)

#Ex4

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list = list1 + list2
print(list)

#Ex5

listofnumbers = [1,2,3,4,10,20,30,-1,5]
print(listofnumbers)
print(min(listofnumbers))
print(max(listofnumbers))


#Ex6

dictionaryofstud = {"John":5, "Michael":6, "Ellen":8}
print(dictionaryofstud["Ellen"])

#Ex7
data = {"John": 17, "Michael": 15, "Ellen": 18}
del data["Michael"]
print(data)
 
#Ex8
data = {"John": 17, "Michael": 15, "Ellen": 18}
print(data.keys)
print(data.values)
 
#Ex9
movies = ("Friends", "Seinfeld", "The Middle")
print(movies)
 
#Ex10
data = (1,2,3)
print(data[0:2])
