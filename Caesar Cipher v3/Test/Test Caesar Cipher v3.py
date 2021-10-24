import time
import MySQLdb as Mysql
import Directorys

with_db = bool(True)
try:
    mydb = Mysql.connect("Server", "Username", "Password", "Name")
    cur = mydb.cursor()
except:
    print("Error to connect with Database!")
    with_db = False


def encrypt_words(string):
    cipher_text = ''
    for index in range(len(string)):
        let = string[index]
        ascii_code = ord(let)
        if let.isupper():
            cipher_text += chr((ord(let) + int(shift) - 65) % 26 + 65)
        elif let.islower():
            cipher_text += chr((ord(let) + int(shift) - 97) % 26 + 97)
        elif let.isdigit():
            cipher_text += chr((ord(let) + int(shift) - 48) % len(Directorys.numbers) + 48)
        else:
            if ascii_code <= 47:
                cipher_text += chr((ord(let) + int(shift) - 32) % len(Directorys.d4) + 32)
            elif 47 < ascii_code <= 64:
                cipher_text += chr((ord(let) + int(shift) - 58) % len(Directorys.d1) + 58)
            elif 64 < ascii_code <= 96:
                cipher_text += chr((ord(let) + int(shift) - 91) % len(Directorys.d2) + 91)
            elif 96 < ascii_code <= 126:
                cipher_text += chr((ord(let) + int(shift) - 123) % len(Directorys.d2) + 123)
    return cipher_text


def decrypt_words(string):
    cipher_text = ''
    for index in range(len(string)):
        let = string[index]
        ascii_code = ord(let)
        if let.isupper():
            cipher_text += chr((ord(let) + int(shift) - 65) % 26 + 65)
        elif let.islower():
            cipher_text += chr((ord(let) + int(shift) - 97) % 26 + 97)
        elif let.isdigit():
            cipher_text += chr((ord(let) + int(shift) - 48) % len(Directorys.numbers) + 48)
        else:
            if ascii_code <= 47:
                cipher_text += chr((ord(let) + int(shift) - 32) % len(Directorys.d4) + 32)
            elif 47 < ascii_code <= 64:
                cipher_text += chr((ord(let) + int(shift) - 58) % len(Directorys.d1) + 58)
            elif 64 < ascii_code <= 96:
                cipher_text += chr((ord(let) + int(shift) - 91) % len(Directorys.d2) + 91)
            elif 96 < ascii_code <= 126:
                cipher_text += chr((ord(let) + int(shift) - 123) % len(Directorys.d2) + 123)
    return cipher_text


def encrypt_files(text_in_line):
    cipher_text = ''
    for index in range(len(text_in_line)):
        let = text_in_line[index]
        ascii_code = ord(let)
        if let.isupper():
            cipher_text += chr((ord(let) + int(shift) - 65) % 26 + 65)
        elif let.islower():
            cipher_text += chr((ord(let) + int(shift) - 97) % 26 + 97)
        elif let.isdigit():
            cipher_text += chr((ord(let) + int(shift) - 48) % len(Directorys.numbers) + 48)
        else:
            if ascii_code <= 47:
                cipher_text += chr((ord(let) + int(shift) - 32) % len(Directorys.d4) + 32)
            elif 47 < ascii_code <= 64:
                cipher_text += chr((ord(let) + int(shift) - 58) % len(Directorys.d1) + 58)
            elif 64 < ascii_code <= 96:
                cipher_text += chr((ord(let) + int(shift) - 91) % len(Directorys.d2) + 91)
            elif 96 < ascii_code <= 126:
                cipher_text += chr((ord(let) + int(shift) - 123) % len(Directorys.d2) + 123)

    return cipher_text + "\n"


def decrypt_file(text_in_line):
    cipher_text = ''
    for index in range(len(text_in_line)):
        let = text_in_line[index]
        ascii_code = ord(let)
        if let.isupper():
            cipher_text += chr((ord(let) + int(shift) - 65) % 26 + 65)
        elif let.islower():
            cipher_text += chr((ord(let) + int(shift) - 97) % 26 + 97)
        elif let.isdigit():
            cipher_text += chr((ord(let) + int(shift) - 48) % len(Directorys.numbers) + 48)
        else:
            if ascii_code <= 47:
                cipher_text += chr((ord(let) + int(shift) - 32) % len(Directorys.d4) + 32)
            elif 47 < ascii_code <= 64:
                cipher_text += chr((ord(let) + int(shift) - 58) % len(Directorys.d1) + 58)
            elif 64 < ascii_code <= 96:
                cipher_text += chr((ord(let) + int(shift) - 91) % len(Directorys.d2) + 91)
            elif 96 < ascii_code <= 126:
                cipher_text += chr((ord(let) + int(shift) - 123) % len(Directorys.d2) + 123)

    return cipher_text + "\n"


def insert(plain, cipher, password):
    try:
        values = (plain, shift, cipher, password)
        cur.execute("INSERT INTO table_db (plain , shift , cipher , password) VALUES (%s,%s,%s,%s)", values)
        mydb.commit()
        flag = True
    except:
        flag = False

    return flag


def get_data_from_db():
    try:
        cur.execute("SELECT * FROM table_db")
        return cur.fetchall()
    except:
        return '''0
    0
    0'''''


def delete_from_db(value1, value2):
    try:
        cur.execute("DELETE FROM table_db WHERE cipher = '{0}' and password = '{1}'".format(value1, value2))
        mydb.commit()
        flag = True
    except:
        flag = False
    return flag


def main():
    global shift
    try:
        if Question == 1:
            plain = "Hello There , This is Version 3 for Caesar Cipher.. Just test"
            cipher = encrypt_words(plain)
            if with_db == False:
                print("The Cipher Text : " + cipher)
            else:
                passwd = "12345"
                if insert(plain, cipher, passwd):
                    print("The Cipher Text : " + cipher)
                else:
                    print("Something wrong!!")
        elif Question == 2:
            cipher = "Mjqqt%Ymjwj%!%Ymnx%nx%Ajwxnts%8%ktw%Hfjxfw%Hnumjw##%Ozxy%yjxy"
            if with_db == False:
                shift -= shift * 2
                plain = decrypt_words(cipher)
                print("Plain Text --> : " + plain)
            else:
                passwd = "12345"
                for data in get_data_from_db():
                    if cipher == data[2] and passwd == data[-1]:
                        if str(shift) == str(data[1]):
                            shift = int(data[1])
                            shift -= shift * 2
                            plain = decrypt_words(data[2])
                            print("Plain Text --> : " + plain)
                            if delete_from_db(data[2], data[-1]):
                                break
                            else:
                                delete_from_db(data[2], data[-1])
                        else:
                            print("Error in Your Shift key !! ")
                    else:
                        print("Error in cipher text or the password!, please try again")
        elif Question == 3:
            file_text = open("msg.txt", "r").read().splitlines()
            [open("Msg-Encrypt.txt", "a").write(encrypt_files(line)) for line in file_text]
            print("[!] message has been protected !!!")
            print("----------------------------------------")
        elif Question == 4:
            shift -= shift * 2
            file_text = open("msg-Encrypt.txt", "r").read().splitlines()
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
    shift = int(5)
else:
    input("You need to enter a valid number !!")
    exit(0)

main()
