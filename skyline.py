def skyline(string):
    """ takes in a string and returns a matching string where
    every letter is uppercase, and every odd letter is lowercase.
    """
    modString = []
    for i in range(len(string)):
        if i % 2 == 0:
            modString.append(string[i].lower())     
        else:
            modString.append(string[i].upper())
    print(modString)
    return "".join(modString)

myString = ('computer')
print(skyline(myString))

def lesserOfTwoEvens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b

print(lesserOfTwoEvens(4,6))