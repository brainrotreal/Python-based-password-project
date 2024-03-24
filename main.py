import json
import os
import time

def create_account():
    print("Account not found, please create an account.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    info = {"user_info": {"username": username, "password": password}}
    with open("info.json", "w") as file:
        json.dump(info, file)

def login(data):
    print("Account found, starting login.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if data["user_info"]["username"] == username and data["user_info"]["password"] == password:
        print("Login successful!")
        return True
    else:
        print("Incorrect username or password.")
        return False

def main():
    control = True
    attempts = 0
    data = {"user_info": {"username": "", "password": ""}}
    
    while control:
        if os.path.exists("info.json") and os.path.getsize("info.json") > 0:
            with open("info.json") as file:
                try:
                    data = json.load(file)
                except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                    data = {"user_info": {"username": "", "password": ""}}
        
        if data["user_info"]["username"] == "":
            create_account()
        else:
            if login(data):
                control = False
            else:
                if attempts >= 3:
                    print("Maximum login attempts reached. Exiting...")
                    control = False
                else:
                    attempts += 1
                    print(f"{3-attempts} attempts remaining.")
main()
