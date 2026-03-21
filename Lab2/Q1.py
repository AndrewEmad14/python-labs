user_input = input("please Enter a string: ")
vowels = ['a','i','o','u','e']
modified_input = user_input
for i in vowels:
    modified_input = modified_input.replace(i,'')

print(modified_input)