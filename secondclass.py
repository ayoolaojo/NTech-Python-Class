fruits = ["apple", "banana","mango"]
newlist = []
for fruit in fruits:
    if "o" in fruit:
        newlist.append(fruit)


newlist =[fruit for fruit in fruits if "o" in fruit]        
print(newlist)


numbers = [x for x in range (10+1) if x % 2 == 0]
print(numbers)

numbers = [100,20,40,61,81]
numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)


 
    
        


                
        
    

    
