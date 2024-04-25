def mean(lf):
    sum1=0
    count=0
    for i in lf:
        count+=1
        num = int(i)
        sum1=num+sum1
    return sum1/count


print("1) Calculate Mean \n2) Calculate Median \n3) Calculate Mode \n4) Calculate Frequency \n5) Quit")
input_user = int(input("Enter the following options: "))

f=open("1000 random numbers for frequency.txt","r")
for line in f:
    line2 = line.replace(",","")
    line_file = list(line2)
line_file.sort()

if input_user == 1:
    print("The average of the list is",int(mean(line_file)))