#Write a function that takes in a list of integers and returns True if it contains 007 in order

def spyGame(nums):
    code = [0,0,7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return code == []
        
        
        
    
print(spyGame([5,0,6,7,0,9,7]))