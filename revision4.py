def encode_and_decode(choice):
    user_input = input("Enter a code: ")
    num = int(input("Enter a number: "))
    list_string = list(user_input)
    encode_string = ""
    sign = -1
    new_list = list(user_input)
    for i in range(0,len(list_string)):
        if choice == "encode":
            sign  = 1
        elif choice == "decode":
            sign = -1
        sum1 = i + (num*sign)
        mod_num = sum1 % len(list_string)
        new_list[mod_num] = list_string[i]
    for i in new_list:
        encode_string = encode_string + i
    return encode_string
    
on = True    
while on == True:
    print("1) Make a code \n2) Decode a message \n3) Quit")
    print("")
    user_selection = input("Enter your selection: ")
    if user_selection == '1':
        print(encode_and_decode("encode"))
    elif user_selection == '2':
        print(encode_and_decode("decode"))
    elif user_selection == '3':
        on = False
    else:
        print("Please enter 1,2,3")
