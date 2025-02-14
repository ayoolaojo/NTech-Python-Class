#Fibonacci 

nth = int(input("input a number : "))
if nth <= 0:
    print("nth should be positive") 
elif nth == 1:
    print(0)  
elif nth == 2:
    print(1)
else:
    fibo = [0,1]
for i in range(2,nth):
    
    fibo.append(fibo[-1] + fibo[-2])
print (fibo[-1])