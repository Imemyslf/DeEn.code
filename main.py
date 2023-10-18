import os
import Encryption
import Decryption

choice = input('1) Encode\n2) Decode\nEnter : ')
match(choice):
    case '1':
        encrypted_text = ''

        os.system('cls')
        encryption_type = input('1) Caesar Cipher\n2) Substitution Cipher\n3) Vigenère Cipher\n4) Transposition Cipher\n5) Public Key Encryption\nEnter : ')

        os.system('cls')
        text = input('Enter text to be encrypted : ')

        match(encryption_type):
            case '1':
                encrypted_text = Encryption.caesar_cipher(text)
            case '2':
                encrypted_text = Encryption.substitution_cipher(text)
            case '3':
                encrypted_text = Encryption.vigenere_cipher(text)
            case '4':
                encrypted_text = Encryption.transposition_cipher(text)
            case '5':
                encrypted_text = Encryption.public_key_encryption(text)
            case _:
                print('Error')
        
        print('Encrypted Text : ', encrypted_text)

    case '2':
        decrypted_text = ''

        os.system('cls')
        decryption_type = input('1) Caesar Cipher\n2) Substitution Cipher\n3) Vigenère Cipher\n4) Transposition Cipher\n5) Public Key Encryption\nEnter : ')

        os.system('cls')
        text = input('Enter text to be decrypted : ')

        match(decryption_type):
            case '1':
                decrypted_text = Decryption.caesar_cipher(text)
            case '2':
                decrypted_text = Decryption.substitution_cipher(text)
            case '3':
                decrypted_text = Decryption.vigenere_cipher(text)
            case '4':
                decrypted_text = Decryption.transposition_cipher(text)
            case '5':
                decrypted_text = Decryption.public_key_decryption(text)
            case _:
                print('Error')
        
        print('Decrypted Text : ', decrypted_text)

    case _:
        print('Error')
