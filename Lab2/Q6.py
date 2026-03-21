isRuning = True
user_stars=""
while isRuning:
    user_stars = input("Enter number of stars: ")
    if user_stars.isdigit():
        user_stars = int(user_stars)
        isRuning = False

line=""
for i in range(user_stars):
    line=""
    for j in range(user_stars):
        if i+j >= user_stars-1:
            line+="*"
        else:
            line+=" "
    print(line)

