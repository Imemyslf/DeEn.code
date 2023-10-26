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

#Prompt user to chosse to encrpyt or decrpyt the message
choice = int(input(" 1. Encode \n 2. Decode \n Enter your choice:-\t"))
if (choice > 0 and choice < 3): #if choice is not > 0 or < 3 then raise the error to user!!.
    y = 0

    while( choice < 3):
        match(choice):
            case 1:
                
                msg = input(" Enter your message to encode:-\t")
                if (len(msg) > 3):
                    # for i in range(len(msg)):
                    #     if(msg[i] == " "):
                    #         msg = msg.replace(msg[i],"!")
                    print(msg)
                    msg = msg[1:] + msg[0]
                    print(msg)
                    msg2 = ""
                    
                    for i in range(len(msg)):
                        if (msg[i] == " "):
                            msg2 = msg2 + "!"
                        else:
                            msg1 = chr(ord(msg[i]) + 100)
                            msg2 = msg2 + msg1
                    print(msg2)
                    msg = msg2
                    l = string.ascii_lowercase
                    msg = ''.join(random.choice(l) for i in range(3)) + msg
                    msg =msg +  ''.join(random.choice(l) for i in range(3)) 
                    print(f"Encoded message is:- {msg}\n")
                    
                    print(f"Do you want to decode this message {msg} \n ")
                    b = input("Press y: yes or n:no\t")
                    if (b == 'y' or b == 'Y'):
                        y = 1
                        choice = 2
                    else:
                        break
                else:
                    msg = msg[::-1]
                    print(f"Encoded message is:- {msg}\n")
                    
                    print(f"Do you want to decode this message {msg} \n ")
                    b = input("Press y: yes or n:no\t")
                    if (b == 'y' or b == 'Y'):
                        y = 1
                        choice = 2
                        msg = msg
                    else:
                        break
            case 2:
                if (y == 1):
                    if (len(msg) < 4):
                        msg = msg[::-1]
                        print(f"Decoded message is:- {msg}")
                        choice = 3
                    else: 
                        msg = msg[3:len(msg) - 3] 
                        msg2 = ""
                        for i in range(len(msg)):
                            if (msg[i] == "!"):
                                msg2 = msg2 + " "
                            else:
                                msg1 = chr(ord(msg[i]) - 100)
                                msg2 = msg2 + msg1
                        msg = msg2 
                        s1 = msg[len(msg)-1]
                        msg = msg.replace(msg[len(msg)-1],"")
                        msg = s1 + msg
                        
                        print(f"Decoded message is:- {msg}")
                        choice = 3
                else:
                    msg = input("Enter your message to decode:-\t")
                    if ( len(msg) < 4):
                        msg = msg[::-1]
                        print(f"Decoded message is:- {msg}")
                        choice = 3
                    else:
                        msg = msg[3:len(msg) - 3] 
                        msg2 = ""
                        for i in range(len(msg)):
                            if (msg[i] == "!"):
                                msg2 = msg2 + " "
                            else:
                                msg1 = chr(ord(msg[i]) - 100)
                                msg2 = msg2 + msg1
                        msg = msg2 
                        s1 = msg[len(msg)-1]
                        msg = msg.replace(msg[len(msg)-1],"")
                        msg = s1 + msg
                        
                        print(f"Decoded message is:- {msg}")
                        choice = 3
            case _:
                print("Invalid choice")
else:
    raise ValueError("Invalid choice")
