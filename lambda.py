# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.
# use a lambda function that will print out map and filter

num = [1,2,3,4,5,6]

newList = [20,40,90,200,3,4,7,100,107,847]

# def Square(x):
#     return x **2

y = map(lambda x: x**2, num)
print(list(y))

    
def even(x):
    if x % 2 == 0:
        return x
z = filter(lambda x:x%2 == 0, num)
print(list(z))

a = filter(lambda x : x % 2 == 1, num)
print(list(a))


half = map(lambda x : x / 2 , num )
print(list(half))

CurList = map(lambda x : x * 3 , newList)
print(list(CurList))

filList = filter(lambda x: x >= 100, newList)
print(list(filList))