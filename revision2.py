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
       if cl[i] not in col_lis:
           col_lis.append(cl[i])
           if i == 3:
               print("HI")
           for j in range(0+i,4):
                
                if ul[j] == col_lis[-1]:
                    not_colour += 1
    print("Correct colour in the wrong place:",not_colour)

    
colours = ["red","blue","green","yellow","pink"]
comp_list = []
user_list = []
count = 0
for i in range(0,4):
    num = random.randint(0,4)
    comp_list.append(colours[num])
    
while count != 4 :
    for i in range(0,4):
        user_guess = input("Enter a colour ")
        user_list.append(user_guess)
    count = check_colour(comp_list,user_list)
    check_colour2(comp_list,user_list)
    