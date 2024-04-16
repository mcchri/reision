def new_user_ID(uids):
    ok=0
    while ok == 0:
        new_id = input("Enter a user ID: ")
        if new_id in uids:
            print("Select another new ID")
        else:
            ok += 1
            uids.append(new_id)
            return uids,new_id
        
def new_password():
        special_list=["!","£","$","%","&","<","*","@"]
        score_list = [0,0,0,0,0]
        score = 0
        count = 0
        new_paswrd = input("Enter a password: ")
        for i in new_paswrd:
            count += 1
            if i.upper() and score_list[0] <1:
                score_list[0] = 1
            elif i.lower() and score_list[1] <1:
                score_list[1] = 1
            elif type(i) == int and score_list[2] <1:
                score_list[2] = 1
            elif i in special_list and score_list[3] <1:
                score_list[3] = 1
        if count > 7:
            score_list[4] = 1
        for i in score_list:
            if i == 1:
                score+=1
        return score,new_paswrd

def GUI():
    ok = 0
    while ok == 0:        
        print("1) Create a new User ID \n2) Change a password \n3) Display all the User Ids \n4) Quit")
        print("")
        selct = int(input("Enter Selection: "))
        user_IDs = []
        correct = False

        if selct == 1:
            ID_lis = new_user_ID(user_IDs)
            user_IDs = ID_lis[0]
            user_ID = ID_lis[1]
            while correct == False:
                lis_pass = new_password()
                score = lis_pass[0]
                if score < 3:
                    print("It is a weak password")
                elif score < 5:
                    print("This password could be improved")
                    choice = input("Do you want to make another password: (yes/no) ")
                    if choice == "no":
                        correct = True
                elif score == 5:
                    print("You have a strong password")
                    correct = True
            f = open("IDs.csv",'w')
            user_ID = user_ID + ","
            string_com = user_ID + lis_pass[1]
            f.write(string_com)
            f.close()
            
        elif selct == 2:
            change_id = input("Enter the existing ID that you want to change the password: ")
            f = open("IDs.csv",'r')
            for line in f:
                x=line.split(",")
                if change_id == x[0]:
                    lis_pass = new_password()
                    f = ''.replace(x[1],lis_pass[1])
            f = open("IDs.csv",'r')
            f.close()
            
        elif selct == 3:
            f = open("IDs.csv",'r')
            for line in f:
                x=line.split(",")
                print(x[0])
        else:
            ok+=1
GUI()
