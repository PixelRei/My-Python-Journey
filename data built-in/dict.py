#a dictionary consist of key and value
d = {"one": 1, "two": 2, "three" : 3}
print(d["one"])
print(d) #if the key doesn't exist it return KeyError
if 'one' in d: #or "not in"
    print("presente")
#to overwrite or delete
d['one'] = 1.1
del d['three']
print(d)

#returning the elements in a tuple
print(d.items())

#returning the keys
print(d.keys())

#and the values
print(d.values())

#returning a copy of the dictionary
copy_d = d.copy()

#adding elements to the dictionary
d1 = {
    "a": 10,
    "b": 20,
    "c": 30
}
d.update(d1)
print(d)

#removing and at the same time returning a value
print(d.pop("a"))
print(d)

#to remove just the last element
d.popitem()

#removing all the elements
d.clear()