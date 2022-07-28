def hello():
    print("Hello")

hello() #呼叫函式

def print_manytimes(str, count):
    for i in range(count):
        print(str)

print_manytimes("Hi", 3)

#return
def add(num1, num2):
    return num1 + num2

print(add(2, 2.5))