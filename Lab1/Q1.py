userInput = input("please Enter a Number: ")
start = 5
end = 10
num = "invalid"
if userInput.isdigit():
    num = int(userInput)

    

if num != "invalid" and num>=start and num<=end:
    print("valid number")
else:
    print("invalid number")