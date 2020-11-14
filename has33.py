#Given a list of integers, return True if the array contains a 3 next to a 3 somewhere

def has33(nums):
    for i in range(len(nums)-1):
        print(i)
        
    return nums[i] == 3 and nums[i + 1] == 3
    #alternatively return nums[i:i+2] == [3,3]
    
    
print(has33([4,3,7,8,3,3]))