#Given a string, return a string where for every character in the original there are 3 characters

def paperDoll(text):
    newWord = ''
    for char in text:
        newWord += char * 3
    return newWord
    
print(paperDoll('Liphook'))