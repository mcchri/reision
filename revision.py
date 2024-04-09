import random
def rand():
    x = random.randint(1,10)
    y = random.randint(1,10)
    return x,y
nums = rand()    
def compare(nums):
    if nums[0] == nums[1]:
        return True
    else:
        return False
compare(nums)    