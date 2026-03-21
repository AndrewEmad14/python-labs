user_input = input("enter your names: ")
names = sorted(user_input.lower().split())
dictionary = {}

for name in names:
    if name[0] in dictionary:
        dictionary[name[0].upper()].append(name)
    else:
        dictionary[name[0].upper()] = [name]

print(dictionary)

