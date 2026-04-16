def is_pangram(s):
    s = s.lower()
    letters = set()
    
    for char in s:
        if 'a' <= char <= 'z':
            letters.add(char)
    print (letters)

    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"
    
print("Enter sentence:")
s = input().strip()

print(is_pangram(s))
