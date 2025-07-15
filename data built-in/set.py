#sets and frozensets consist of unique elements, and we can change tha value of a set
#creating a set
s = {1,2,3, "wassup"}
#creating a frozenset
fs = frozenset(s) #or frozenset([1,2,3,"wassup"])

#we have the same methods len(), max(), min()

#adding elements to a set
s.add(False)

#then removing (returns none if the element doesn't exist)
s.remove(0)

#still removing, only if the element exist (no error if it doesn't)
s.discard(1)

#removing and returning the last element
s.pop()

#returning a copy of the set
copy_set = s.copy()

print(s)
#removing all elements
s.clear()