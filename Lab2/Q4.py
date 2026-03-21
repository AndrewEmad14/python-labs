# t r r c
options = ['t','r','c']

def calaculate_area(option, *dimensions):
    found = False
    for i in options:
        if i == option:
            found = True
    
    if not found:
        print("please Enter a correct option t|r|c")
        return
    
    if option == 't':
        return dimensions[0]*dimensions[1]*0.5
    elif option == 'r':
        if len(dimensions) == 2:
            return dimensions[0]*dimensions[1]
        else:
            return dimensions[0]*dimensions[0]
    else:
        return dimensions[0]*dimensions[0]*3.14
    


user_shape = input("Enter your shape (t|r|c): ")

isRunning = True
user_dimensions=''
while isRunning:
    user_dimensions = input("Enter your dimensions: ")
    dimensions = user_dimensions.split()
    isRunning = False
    for i in range(0,len(dimensions)):
        if(dimensions[i] and dimensions[i].isdigit()):
            dimensions[i] = int(dimensions[i])
        else:
            isRunning = True
            print("Please Enter a valid number")
        


print(calaculate_area(user_shape,*dimensions))


