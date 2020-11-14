#Returns the lesser of 2 given numbers if both numbers are even, but returns greater
#if one or both numbers are odd

def lesserOfTwoEvens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print(lesserOfTwoEvens(5,7))