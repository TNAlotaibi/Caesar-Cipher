def encrypt():
    cipher_text = ''
    for index in range(len(plain_text)):
        let = plain_text[index]
        if let.isspace():
            cipher_text += " "
        elif let.isupper():
            cipher_text += chr((ord(let) + int(shift) - 65) % 26 + 65)
        else:
            cipher_text += chr((ord(let) + int(shift) - 97) % 26 + 97)

    return cipher_text


print(" ------------------------------ ")
print("|         Caesar Cipher        |")
print(" ------------------------------ ")
plain_text = "Hello World Just Test Caesar Cipher"
shift = int(3)
cipher_text = encrypt()
print("The Cipher Text : " + cipher_text)
#Khoor Zruog Mxvw Whvw Fdhvdu Flskhu  < - - - - - Result
