# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string

a = int(input(" 1. Encode \n 2. Decode \n Enter your choice:-\t"))
if (a > 0 and a < 3):
    msg2 = ""
    y = 0
    x = True

    while( a < 3):
        match(a):
            case 1:
                
                msg = input(" Enter your message to encode:-\t")
                if (len(msg) > 3):
                    s = msg[0]
                    s1=msg.replace(msg[0],"")
                    msg2 = s1 + s
                    l = string.ascii_lowercase
                    msg2 = ''.join(random.choice(l) for i in range(3)) + msg2
                    msg2 =msg2 +  ''.join(random.choice(l) for i in range(3)) 
                    print(f"Encoded message is:- {msg2}\n")
                    
                    print(f"Do you want to decode this message {msg2} \n ")
                    b = input("Press y: yes or n:no\t")
                    if (b == 'y' or b == 'Y'):
                        y = 1
                        a = 2
                        msg = msg2
                    else:
                        break
                else:
                    msg = msg[::-1]
                    print(f"Encoded message is:- {msg}\n")
                    
                    print(f"Do you want to decode this message {msg} \n ")
                    b = input("Press y: yes or n:no\t")
                    if (b == 'y' or b == 'Y'):
                        y = 1
                        a = 2
                        msg = msg
                    else:
                        break
            case 2:
                if (y == 1):
                    if (len(msg) < 4):
                        msg = msg[::-1]
                        print(f"Decoded message is:- {msg}")
                        a = 3
                    else:
                        msg = msg[3:len(msg) - 3]
                        s1 = msg[len(msg)-1]
                        msg = msg.replace(msg[len(msg)-1],"")
                        msg = s1 + msg
                        print(f"Decoded message is:- {msg}")
                        a = 3
                else:
                    msg = input("Enter your message to decode:-\t")
                    if ( len(msg) < 4):
                        msg = msg[::-1]
                        print(f"Decoded message is:- {msg}")
                        a = 3
                    else:
                        msg = msg[3:len(msg) - 3]
                        s1 = msg[len(msg)-1]
                        msg = msg.replace(msg[len(msg)-1],"")
                        msg = s1 + msg
                        print(f"decoded message is:- {msg}")
                        a = 3
            case _:
                print("Invalid choice")
else:
    raise ValueError("Invalid choice")
