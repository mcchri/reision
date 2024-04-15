import random

def check_colour(cl,ul):
    colour_place = 0
    for i in range(0,4):
        if cl[i] == ul[i]:
           colour_place += 1
    print("Correct colour in the correct place:",colour_place)       
    return colour_place

def check_colour2(cl,ul):
    col_lis = []
    
    not_colour = 0
    for i in range(0,4):
       ok=0
       if cl[i] not in col_lis:
           col_lis.append(cl[i])
           for j in range(0+i,4):
                
                if ul[j] == col_lis[-1] and ok != 1:
                    not_colour += 1
                    ok+=1
    print("Correct colour in the wrong place:",not_colour)

    
colours = ["red","blue","green","yellow","pink"]
comp_list = []
count_guess = 0
count = 0
for i in range(0,4):
    num = random.randint(0,4)
    comp_list.append(colours[num])
    
while count != 4 :
    user_list = []
    for i in range(0,4):
        user_guess = input("Enter a colour ")
        count_guess += 1
        user_list.append(user_guess)
    count = check_colour(comp_list,user_list)
    check_colour2(comp_list,user_list)
print("You got the correct match, it took you",count_guess,"guesses.")    
