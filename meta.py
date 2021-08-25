# This is a sample Python script.
import importlib
import os.path
import inspect

from importlib import import_module


def decorator(original_func):  # the outer function that gets a function as parameter
    def wrapper(*args, **kwargs):  # inner function that uses the original function but wraps it
        temp_str = original_func(*args, **kwargs)  # original function execution
        print(temp_str)  # print func output
        print('Added code!')  # work after running

    return wrapper  # return edited function


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    f = open("demofile.txt", "r")
    print(f.read())


# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    file_path = "fruit.py"
    # Validation of exists file
    while True:
        # file_path = input("Enter python file name:")
        file_path = "fruit.py"
        if os.path.isfile(file_path):
            break

    file = open(file_path, "r")
    name_file = file_path[0:-3]
    cs = importlib.import_module(name_file, file_path)

    # Find all classes Objects!

    name, obj = inspect.getmembers(cs)[0]
    for func_name, func in obj.__dict__.items():
        if callable(func):
            print(func_name)
            setattr(obj, func_name, decorator(func))

# Main code run obj
    AppleBasket = obj
    InstA = AppleBasket("red", 4)
    InstB = AppleBasket("blue", 50)

    FruitBasket = [InstA, InstB]
    for fruit in FruitBasket:
        print(fruit)
