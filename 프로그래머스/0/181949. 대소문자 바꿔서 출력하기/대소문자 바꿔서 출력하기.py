s = input()
result =""
for char in s:
    if char.islower():
        result+=char.upper()
    else:
        result+=char.lower()
        
print(result)