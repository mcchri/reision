def mean(lf):
    sum1=0
    count=0
    for i in range(0,len(lf)):
        if "#" in lf[i]:
            num = (int(lf[i-1] + lf[i+1]))//2
            count+=1
        elif "/" in lf[i]:
            num=0
        else:
            num=int(lf[i])
            count+=1
        sum1=num+sum1
    return sum1/count

def median(lf):
    if len(lf) % 2 == 0:
        med = lf[(len(lf)/2)+((len(lf)/2)+1)]
        med = med // 2
    else:
        med = lf[((len(lf)+1)/2)]
    return med        
        
print("1) Calculate Mean \n2) Calculate Median \n3) Calculate Mode \n4) Calculate Frequency \n5) Quit")
input_user = int(input("Enter the following options: "))

f=open("1000 random numbers - corrupted 1.txt","r")
print(f)
for line in f:
    line2 = line.replace(",","")
    line_file = line2.split(" ")
line_file.sort()

if input_user == 1:
    print("The average of the list is",int(mean(line_file)))
elif input_user == 2:
    print("The median of the list is",int(median(line_file)))
#elif    
