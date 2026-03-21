user_input = input("Enter a string: ")
target = input("Enter a target: ")
result=[]
for i in range(len(user_input)):
    if user_input[i] == target:
        result.append(i)

print(result)