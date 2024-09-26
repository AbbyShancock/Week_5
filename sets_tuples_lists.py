#collections = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but add/remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)
#prints ['apple', 'orange', 'banana', 'coconut']
print(fruits[0]) #first word would have an index of 0, so apple would be 0.
#prints apple
print(fruits[0:3])
#prints ['apple', 'orange', 'banana']
print(fruits[1:])
# prints ['orange', 'banana', 'coconut']


fruits2 = ["apple", "orange", "banana", "coconut", "strawberry", "grapes"]
print(fruits2[::2]) #gives me every second element in the list
#prints ['apple', 'banana', 'strawberry']
print(fruits2[::-1]) #gives me the list backwards. (reverses it)
#prints ['grapes', 'strawberry', 'coconut', 'banana', 'orange', 'apple']

#iteration
#fruit = apple
#fruit = orange
#fruit = banana
#fruits = coconut
#going through a list and doing something with it.
for fruit in fruits2:
    print(fruit)


print(dir(fruits2)) #listing out all the atributes. Gives you all the attributes for the list
#prints ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(help(fruits2)) #gives you helpful documentation.
print(len(fruits2)) #gives you the length of how many elements in the list
#prints 6
print("apple" in fruits2) #tells you if this element (apples) is in your list
#prints True

fruits2[0] = "dragonfruit" #first element/value (was apple) is now dragonfruit
for fruit in fruits2:
    print(fruit)

fruits2.append("pineapple") #adds element to the END of the list
fruits2.remove("apple") #removes element from a list.
fruits2.insert(0, "pineapple") #INSERTS something in the 0 spot. so now pineapple has the index of 0.
#insert does NOT replace.
fruits2.sort() #puts everything in alphabetical order
fruits2.reverse() #reverses in the order 
fruits2.clear() #clears everything
print(fruits.index("apple")) #returns it to an index