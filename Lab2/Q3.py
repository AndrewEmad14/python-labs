# 1 -> [1]
# 2 -> [1],[2,4]
# 3 -> [1],[2,4],[3,6,9]

isRuning = True

while isRuning:
    user_input = input("Enter a number: ")
    
    if not user_input.isdigit():
        print("please enter a digit!")
    else:
        isRuning = False

target = int(user_input)
multiplication_table = []
for i in range(1,target+1):
    row = []
    for j in range(1,i+1):
        row.append(i*j)
    multiplication_table.append(row)

print(multiplication_table)