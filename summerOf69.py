#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
#and extending tot he next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers

def summerOf69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True           
    return total
        
        
    
print(summerOf69([5,5,6,7,8,9,10]))