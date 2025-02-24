#Tuples are ordered amd indexed but not changeable

names = ("Ola","Messi", "Ayoola", "Iyanu") #this is a tuple

#tuple is not changeable, to addnto a tuple, convert to list, add to the list and then convert back to tuple.

names = list(names)
names.append("Olasco")

names = tuple(names)

print(names)

print(names[2:])

colors= ("blue","green", "yellow")
(first,*other) = colors
print(first)
print