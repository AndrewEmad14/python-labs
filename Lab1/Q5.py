isRunning = True

while isRunning:
    name = input("Enter YOur Name: ")

    if not name:
        print("please Enter your name")
    else:
        isRunning = False



isRunning = True

while isRunning:
    age = input("Enter your age: ")

    if age.isdigit():
        isRunning = False
    else:
        print("age must be a number")

print(name +" is "+age+" years old")
