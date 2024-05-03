user_input = input("Enter a single character: ")
print(f"ASCII value of {user_input}, {ord(user_input)}")
print(f"Unicode value of {user_input}, {ord(user_input)}")

message = ("abcdefghijklmonopqrstuvwxyz")
string_message = ""
num_message = []
count = 0
for i in message:
    encoded = ord(i)
    if i == "y":
        print("")
    if len(message)-count < 3:
        encoded = encoded - len(message) + 1
    num_message.append(encoded+2)
    string_message = string_message + chr(num_message[count])
    count += 1
print(string_message)    