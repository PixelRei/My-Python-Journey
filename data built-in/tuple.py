turtle = ()
#print(type(turtle))
#we get the elements in the same way we do with lists
#we do the same also for slicing

#tuples are immutable, which means that we can't add or remove items, so we can just manipulate data
turtle = ('abc', 1,2,3, "kebab", True)
print(turtle)
print(turtle[len(turtle)-1])
print(turtle[::-1]) 
print(turtle[0], ", ", turtle[2:]) #all the elements except the index 1

#we can also get the max and min, if we have the same type of data for all elements
#print(max(turtle))
#print(min(turtle))