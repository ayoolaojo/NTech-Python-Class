 






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


yourInput = input("type an alphabet :").lower()
if len(yourInput) != 1 and yourInput != yourInput.isalpha():
    print("invalid input, please enter a single alphabet")
else:
    print("")
    
vowel = ["a", "e", "i", "o", "u"]    
    
        


                
        
    

    
