from tkinter import *
import tkinter.messagebox
import customtkinter
from customtkinter import *
from DeEn import dean

app = CTk()
window = CTkFrame(app)
window.pack(padx=20, pady=20)


label_1 = customtkinter.CTkLabel(window,text="Ki's-cryption", font=("Arial Unicode MS", 30,"bold"))
label_1.grid(row=0,column=0,columnspan=3, padx=10, pady=10)

label_2  = customtkinter.CTkLabel(window,text="Decrypted message",font=("Arial Unicode MS", 15))
label_2 .grid(row=1,column=0)

label_2  = customtkinter.CTkLabel(window,text="Encrypted message",font=("Arial Unicode MS", 15))
label_2 .grid(row=1,column=2)


encryption = customtkinter.CTkTextbox(window, border_width=2, corner_radius=20,border_color="green",text_color="#FF783F")
encryption.insert("0.0", "")  
encryption.grid(row=2, column=0, padx=(10,0), pady=(0,20))

decryption = customtkinter.CTkTextbox(window, border_width=2, corner_radius=20,border_color="red",text_color="#FF783F")
decryption.insert("0.0", "")  
decryption.grid(row=2, column=2, padx=(10, 10), pady=(0,20))

def button_1():
    decryption.delete("0.0",customtkinter.END)
    encrypted_text = encryption.get("1.0", "end-1c")  # Get the text from the encryption Textbox
    encrypted_message = dean(encrypted_text,1)
    decryption.insert("0.0",encrypted_message)
    encryption.delete("0.0",customtkinter.END)

def button_2():
    encryption.delete("0.0",customtkinter.END)
    decrypted_text = decryption.get("1.0", "end-1c")  # Get the text from the encryption Textbox 
    decrypted_message = dean (decrypted_text,2)
    encryption.insert("0.0",decrypted_message)
    decryption.delete("0.0",customtkinter.END)

encrypt_button = customtkinter.CTkButton(window,text="Encrypt",command = button_1)
encrypt_button.grid(row=4, column=0, padx=10, pady=(0,10))

decrypt_button = customtkinter.CTkButton(window,text="Decrypt",command = button_2)
decrypt_button.grid(row=4, column=2, padx=10, pady=(0,10))
app.mainloop()