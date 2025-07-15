MyList = []
MyList.append(21)
#to add an item
MyList.append("ciao")
print(MyList)
print(len(MyList))
#to delete an item
del MyList[1] #or just use remove(element)
print(MyList)

#finding the max and the min
MyList = [1,2,3,12,45,456,12,-140]
print("max: ", max(MyList))
print("min: ", min(MyList))

#extending a list adding another one
seq = [10,20,30,40]
MyList.extend(seq)
print("lista estesa: ", MyList)

#inserting an item in a specific index
MyList.insert(0, "hola!")
print(MyList)

#getting and also removing the last element
print(MyList.pop())
print(MyList)