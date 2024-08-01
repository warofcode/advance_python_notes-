def first_function():
    return "I am from first module"

if __name__ =="__main__":

    print("This print statement is in",__name__)

    print(first_function())