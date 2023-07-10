string = input("enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for char in string:
    if char not in vowels:
        result += char

print('string with vowels removed:', result)
     