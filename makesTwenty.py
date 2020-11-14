#given two integers, return True if their sum is 20 or if one of the integers is 20, if not, return false

def makesTwenty(a,b):
    return sum((a,b)) == 20 or a == 20 or b == 20
        

print(makesTwenty(5, 20))