import time

def timer(func):
    def wrapper(*args, **kwargs):
        # print(args,"*args")
        # print(kwargs,"**kwargs")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def long_task():
    time.sleep(2)
    print("Task complete!")

@timer
def long_task1():
    time.sleep(4)
    print("Task complete!")

long_task()
long_task1()
