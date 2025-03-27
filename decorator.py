#code starts
#Greetings, hellonguys
3# done

def decorator_func(func):
    def wrapper():
        print("Code Starts")
        func()
        print("done!!!")
    return wrapper


@decorator_func
def greetings():
    return "Greetings, Hello guys!"

greetings()


def decorator_add(func):
    def wrapper(*args, **kwargs):
        print("...adding two numbers")
        func(*args,**kwargs)
        print("Done!!!")
    return wrapper



def add(a,b):
    return a + b

#**********************









