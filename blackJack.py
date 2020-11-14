#Given 3 ints between 1 and 11, if their sum is less than or equal to 21,
#return their sum, if their sum exceeds 21 and there is an eleven, reudce the total sum by 10,
#if the sum (even after the adjustment) exceeds 21, return 'BUST".

def blackJack(a,b,c):
    if sum([a,b,c]) <= 2:
        return sum([a,b,c])
    else:
        if 11 in (a,b,c) and sum([a,b,c]) <= 31:
            return sum([a,b,c]) - 10
        else:
            return "BUST"
        
    
print(blackJack(10,11,11))