import random
import string

def dean( msg, choice):
    if (choice > 0 and choice < 3): #if choice is not > 0 or < 3 then raise the error to user!!.
        # yes = 0 
        while( choice < 3):
            match(choice):
                case 1:
                    
                    # msg = input(" Enter your message to encode:- (Press ENDD to end the text!!)\n")
                    # while True:
                    #     line = input("")
                    #     if line == "ENDD":
                    #         break
                    #     msg += line + "\n"
                    msg = msg[1:] + msg[0]
                    msg2 = ""
                        
                    for i in range(len(msg)):
                        if (msg[i] == " "):
                            msg2 = msg2 + "!"
                        elif (msg[i] == "\n"):
                            msg2 = msg2 + "`"
                        else:
                            msg1 = chr(ord(msg[i]) + 100)
                            msg2 = msg2 + msg1
                    msg = msg2
                    l = string.ascii_lowercase
                    msg = ''.join(random.choice(l) for i in range(3)) + msg
                    msg =msg +  ''.join(random.choice(l) for i in range(3)) 
                    # print(f"Encoded message is:- \n {msg}\n")
                    choice = 3
                    return msg
                    
                    # print(f"Do you want to decode this message {msg} \n ")
                    # b = input("Press y: yes or n:no\t")
                    # if (b == 'y' or b == 'Y'):
                    #     yes = 1
                    #     choice = 2
                    # else:
                    #     break
                case 2:
                    # if (yes == 1):
                    #         msg = msg[3:len(msg) - 3] 
                    #         msg2 = ""
                    #         for i in range(len(msg)):
                    #             if (msg[i] == "!"):
                    #                 msg2 = msg2 + " " 
                    #             elif (msg[i] == "`"):
                    #                 msg2 = msg2 + "\n"
                    #             else:
                    #                 msg1 = chr(ord(msg[i]) - 100)
                    #                 msg2 = msg2 + msg1
                                
                    #         msg = msg2 
                    #         s1 = msg[len(msg)-1]
                    #         msg = msg.replace(msg[len(msg)-1],"")
                    #         msg = s1 + msg
                            
                    #         print(f"Decoded message is:- \n {msg}")
                    #         choice = 3
                    #  else:
                    #     msg = input("Enter your message to decode:-\t")
                        msg = msg[3:len(msg) - 3] 
                        msg2 = ""
                        for i in range(len(msg)):
                            if (msg[i] == "!"):
                                msg2 = msg2 + " "
                            else:
                                msg1 = chr(ord(msg[i]) - 100)
                                msg2 = msg2 + msg1
                        msg = msg2 
                        # s1 = msg[len(msg)-1]
                        # msg = msg.replace(msg[len(msg)-1],"")
                        # msg = s1 + msg
                        
                        msg = msg[len(msg)-1] + msg[0:len(msg)-1]
                        choice = 3
                        return msg
                case _:
                    print("Invalid choice")
    else:
        raise ValueError("Invalid choice")