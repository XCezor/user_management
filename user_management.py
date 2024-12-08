import json
import random
import re
import os

file_path = "data/users.json"

def load_data():
    '''
    Check if the file and folder exists. If exists, loads the data. If not, creates the file and an empty list.
    '''
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    data = []
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    return data

def add_user(user_data):
    '''
        Loads data from the .json file, creates new user with provided data and saves them to the file.
    '''
    # Load existing data
    data = load_data()

    # Add new user
    if data:
        user_data["id"] = data[-1]["id"] + 1
    else:
        user_data["id"] = 1

    data.append(user_data)

    # Save new user to the file
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("User created successfully!")

def remove_user(user_id):
    pass

def edit_user(user_id, updated_data):
    pass

def validate_nip(nip):
    pass

def validate_pesel(pesel):
    pass

def validate_regon(regon):
    pass

def generate_password():
    pass

def validate_password(password):
    pass

print("Welcome to the user registration!")
app_running = True
while app_running:
    option = int(input(f"What would you like to do?\n1. Register\n"))
    if option == 1:
        user_data_list = {}
        user_data_list["id"] = 1
        user_data_list["username"] = input("Enter your full name: ")
        user_data_list["nip"] = input("Enter your NIP: ")
        user_data_list["pesel"] = input("Enter your PESEL: ")
        user_data_list["regon"] = input("Enter your Regon number: ")
        user_data_list["password"] = input("Create strong password: ")
        user_data_list["status"] = "Active"

        add_user(user_data_list)