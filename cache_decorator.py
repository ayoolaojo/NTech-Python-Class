import time

def cache_decorator(func):
    cache = {} 
    
    def wrapper(*args):
        if args in cache:
            print("Returning cached result...")
            return cache[args]
        print(f"computing results for {args}....")
        time.sleep(4)
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@cache_decorator
def expensive_operation(x):
    return x * x


print(expensive_operation(5))
print(expensive_operation(10))
print(expensive_operation(5))
print(expensive_operation(10))

