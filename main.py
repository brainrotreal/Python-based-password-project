# Hewe w-w-we impowt the *boops your nose* wibwawies used in the *boops your nose* code. Json fow the *boops your nose* passwowd/usewnyame stowage, os fow cweawing the *boops your nose* scween and time fow sweeping (deways).
import json
import os
import time

# Cweate account function
def create_account():
    # This function wiww onwy wun if an account is nyot found w-w-when the *boops your nose* usew stawts the *boops your nose* pwogwam.
    print("Account not found, please create an account.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Hewe the *boops your nose* code writes the *boops your nose* usew's input passwowd ^-^ and usewname to the *boops your nose* json fiwe, and nyo I didnt add a check to see if the *boops your nose* passwowd ^-^ is v-vawid because I hate wegex.
    info = {"user_info": {"username": username, "password": password}}
    with open("info.json", "w") as file:
        json.dump(info, file)

# Lwogin fwunction OwO
def login(data):
    # This function onwy wuns ÚwÚ if an account is found w-w-when the *boops your nose* usew stawts the *boops your nose* pwogwam.
    print("Account found, starting login.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # This checks to see if the *boops your nose* inputed usewnyame/passwowd :3 matches the *boops your nose* usewnyame/passwowd :3 on the *boops your nose* json fiwe.
    if data["user_info"]["username"] == username and data["user_info"]["password"] == password:
        print("Login successful!")
        return True
    else:
        print("Incorrect username or password.")
        return False

def main():
    # Vawiabwes fow the code to wowk UwU
    control = True
    attempts = 0
    data = {"user_info": {"username": "", "password": ""}}
    
    # Whiwe woop to contwow the pwogwam fwow >w<
    while control:
        # Load usew data fwom json fiwe if it exists owo
        if os.path.exists("info.json") and os.path.getsize("info.json") > 0:
            with open("info.json") as file:
                try:
                    data = json.load(file)
                except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                    data = {"user_info": {"username": "", "password": ""}}
        
        # Cweate nyew account if nyo usewname is found OwO
        if data["user_info"]["username"] == "":
            create_account()
        else:
            # Wogin check and update attempts uwu
            if login(data):
                control = False
            else:
                # Attempt check UwU
                if attempts >= 3:
                    print("Max wogin attempts! Exiting >_<")
                    control = False
                else:
                    attempts += 1
                    print(f"{3-attempts} attempts wemaining.")
# Wun twe cwode :3
main()
