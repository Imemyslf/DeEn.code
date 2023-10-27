import random
import string

def dean( msg, choice):
    if (choice > 0 and choice < 3): #if choice is not > 0 or < 3 then raise the error to user!!.
        # yes = 0 
        while( choice < 3):
            match(choice):
                case 1:
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
                case 2:
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