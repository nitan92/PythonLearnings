name = input("Enter a name: ")  # naman
reverse = ''
for i in range(len(name) - 1, -1, -1):
    reverse = reverse + name[i]

print(reverse)