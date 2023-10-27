from tkinter import *
import tkinter.messagebox
import customtkinter
from customtkinter import *
from DeEn import dean
app = CTk()

label_1 = customtkinter.CTkLabel(app,text="Encryption and Decryption", font=("Rupee Foradian", 25,"bold"))
label_1.grid(row=0,column=0,columnspan=3)

label_2  = customtkinter.CTkLabel(app,text="Encrypted message")
label_2 .grid(row=1,column=0)

label_2  = customtkinter.CTkLabel(app,text="Decrypted message")
label_2 .grid(row=1,column=2)


encryption = customtkinter.CTkTextbox(app, border_width=3)
encryption.insert("0.0", "")  
encryption.grid(row=2, column=0)

label_3 = customtkinter.CTkLabel(app,text="   ")
label_3.grid(row=2,column=1)

decryption = customtkinter.CTkTextbox(app, border_width=3)
decryption.insert("0.0", "")  
decryption.grid(row=2, column=2)

def button_1():
    encrypted_text = encryption.get("1.0", "end-1c")  # Get the text from the encryption Textbox
    encrypted_message = dean(encrypted_text,1)
    print(f"Encrypted Message:- \n {encrypted_message}")
    # print(encryption.get(1.0, customtkinter.END))

encrypt_button = customtkinter.CTkButton(app,text="Encrypt",command = button_1)
encrypt_button.grid(row=4, column=0)

label_5 = customtkinter.CTkLabel(app,text="")
label_5.grid(row=3, column=0)
label_6 = customtkinter.CTkLabel(app,text="")
label_6.grid(row=3, column=2)

def button_2():
    decrypted_text = decryption.get("1.0", "end-1c")  # Get the text from the encryption Textbox
    decrypted_message = dean (decrypted_text,2)
    print(f"Decrypted Message:- \n {decrypted_message}")

decrypt_button = customtkinter.CTkButton(app,text="Decrypt",command = button_2)
decrypt_button.grid(row=4, column=2)
app.mainloop()