import random
def rand():
    x = random.randint(1,10)
    return x
nums = rand()    
def compare(num1,num2):
    if num1 == num2:
        return True
    else:
        return False

answer = False
while answer != True:
    guess = int(input("Guess the number"))
    answer = compare(nums, guess)
print("YOU WIN!")    
