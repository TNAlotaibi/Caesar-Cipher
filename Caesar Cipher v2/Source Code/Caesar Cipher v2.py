def encrypt_words(string):
    cipher_text = ''
    for index in range(len(string)):
        let = string[index]
        if let.isupper():
            cipher_text += chr((ord(let) + int(shift) - 65) % 26 + 65)
        elif let.islower():
            cipher_text += chr((ord(let) + int(shift) - 97) % 26 + 97)
        else:
            cipher_text += let

    return cipher_text


def decrypt_words(string):
    cipher_text = ''
    for index in range(len(string)):
        let = string[index]
        if let.isupper():
            cipher_text += chr((ord(let) + int(shift) - 65) % 26 + 65)
        elif let.islower():
            cipher_text += chr((ord(let) + int(shift) - 97) % 26 + 97)
        else:
            cipher_text += let
    return cipher_text


def encrypt_files(text_in_line):
    cipher_text = ''
    for index in range(len(text_in_line)):
        let = text_in_line[index]
        if let.isupper():
            cipher_text += chr((ord(let) + int(shift) - 65) % 26 + 65)
        elif let.islower():
            cipher_text += chr((ord(let) + int(shift) - 97) % 26 + 97)
        else:
            cipher_text += let

    return cipher_text + "\n"


def decrypt_file(text_in_line):
    cipher_text = ''
    for index in range(len(text_in_line)):
        let = text_in_line[index]
        if let.isupper():
            cipher_text += chr((ord(let) + int(shift) - 65) % 26 + 65)
        elif let.islower():
            cipher_text += chr((ord(let) + int(shift) - 97) % 26 + 97)
        else:
            cipher_text += let

    return cipher_text + "\n"


def main():
    global shift
    try:
        if Question == 1:
            plain = input("Enter The Word : ")
            cipher = encrypt_words(plain)
            print("The Cipher Text : " + cipher)
        elif Question == 2:
            shift -= shift * 2
            cipher = input("Enter The Word : ")
            print("Cipher Text --> : " + encrypt_words(cipher))
        elif Question == 3:
            file_text = open(input("Enter the file name without .txt --> ") + ".txt", "r").read().splitlines()
            [open("Msg-Encrypt.txt", "a").write(encrypt_files(line)) for line in file_text]
            print("[!] message has been protected !!!")
            print("----------------------------------------")
        elif Question == 4:
            shift -= shift * 2
            file_text = open(input("Enter the file name without .txt --> ") + ".txt", "r").read().splitlines()
            [open("Msg-Decrypt.txt", "a").write(decrypt_file(line)) for line in file_text]
            print("[!] message has been Decrypt !!!")
            print("----------------------------------------")

        else:
            input("You need to enter a valid number !!")
            exit(0)

    except ValueError:
        input("Please Enter the number not the name !!")
        exit(0)


print('''                     ===================================
                    |            Caesar Cipher          |
                     ===================================


    [1] Encrypt Words You copied          [2] Decrypt Words You Copied 
    [3] Encrypt File Text                 [4] Decrypt File Text
    
-----------------------------------------------------------------------------------
 ''')
Question = int(input("===> "))
if Question <= 4:
    shift = int(input("Enter The Key : "))
else:
    input("You need to enter a valid number !!")
    exit(0)

main()
