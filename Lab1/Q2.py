isRunning = True
while isRunning:
    age = input("Please Enter your age: ")
    if age.isdigit():
        age = int(age)
        isRunning = False

copun = input("Please Enter your Copun: ")

if age < 18 or age > 65 or copun:
    print("true")
else:
    print("false")

    

