import random
import string
def dean( msg, choice):
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
                    return msg
                case 2:
                        msg = msg[3:len(msg) - 3] 
                        msg2 = ""
                        for i in range(len(msg)):
                            if (msg[i] == "!"):
                                msg2 = msg2 + " "
                            elif (msg[i] == "`"):
                                msg2 = msg2 + "\n"
                            else:
                                msg1 = chr(ord(msg[i]) - 100)
                                msg2 = msg2 + msg1
                        msg = msg2 
                        msg = msg[len(msg)-1] + msg[0:len(msg)-1]
                        return msg
                case _:
                    print("Invalid choice")