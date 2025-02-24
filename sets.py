#sets are not changeable, not indexed and cannot be duplicated
gadgets = {"radio","televison","laptop"}
len(gadgets)
print(gadgets)

for x in gadgets:
    print(x)
    
for radio in gadgets:
    print(radio in gadgets)
    
gadgets.add("camera")
print(gadgets)

gadgets = list(gadgets)
gadgets.append("ipad")
gadgets =set(gadgets)
print(gadgets)

gadgets.discard("laptop")
print(gadgets)

colors=["yellow","blue"]

gadgets.update(colors)
print(gadgets)
