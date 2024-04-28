def mean(lf):
    sum1=0
    count=0
    for i in range(0,len(lf)):
        if "#" in lf[i]:
            num = (int(lf[i-1]) + int(lf[i+1]))//2
            count+=1
        elif "/" in lf[i]:
            num=0
        else:
            num=int(lf[i])
            count+=1
        sum1=num+sum1
    return sum1/count

def median(lf):
    
    new_lf=[]
    
    for i in range(0,len(lf)):
        if "#" in lf[i]:
            num = (int(lf[i-1]) + int(lf[i+1]))//2
            new_lf.append(num)
        elif "/" in lf[i]:
            num=0
        else:
            num=int(lf[i])
            new_lf.append(num)
    new_lf.sort()
    
    if len(new_lf) % 2 == 0:
        print(len(new_lf))
        med = int(new_lf[int(((len(new_lf)/2)+((len(new_lf)/2)+1))//2)])
        med = med // 2
    else:
        med = new_lf[((len(new_lf)+1)/2)]
    return med        

def mode(lf):
    dict_val = {}
    max_num = 0
    max_str = ""
    count = 0
    for i in range(0,len(lf)):
        num=lf[i]
        if num not in dict_val:
            dict_val[num] = 0
        dict_val[num] += 1   
        if dict_val[num] > max_num:
            max_num = dict_val[num]
            max_str = num
    return max_str

def freq(lf):
    dict_val = {}
    count = 0
    for i in range(0,len(lf)):
        num=lf[i]
        if num not in dict_val:
            dict_val[num] = 0
        dict_val[num] += 1   
    return dict_val
ok=0
while ok!=1:
    print("1) Calculate Mean \n2) Calculate Median \n3) Calculate Mode \n4) Calculate Frequency \n5) Quit")
    input_user = int(input("Enter the following options: "))

    f=open("1000 random numbers - corrupted 1","r")

    for line in f:
        line2 = line.replace(",","")
        line_file = line2.split(" ")
        
    g=open("1000 random numbers for frequency.txt","r")

    for line in g:
        line2 = line.replace(","," ")
        line_file2 = line2.split(" ")
        
    if input_user == 1:
        print("The average of the list is",int(mean(line_file)))

    elif input_user == 2:
        print("The median of the list is",int(median(line_file)))
    elif input_user == 3:
        print("The mode number of this list is",mode(line_file))
    elif input_user == 4:
        print("The frequency of this list is")
        dict_1 = freq(line_file2)
        list_freq=[]
        for i in range(0,11):
            index = str(i)
            val = dict_1.get(index)
            if i > 9:
                print(i," ",val)
            else:    
                print(i,"  ",val)
    else:
        ok+=1

