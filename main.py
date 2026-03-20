from system import system
from utilities import clear_screen
from colorama import Fore,Style
import time
import json

print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Welcome to USER MANAGEMENT SYSTEM......." + Style.RESET_ALL)
sys = system()

#Loading Data From a JSON file before the main program runs into class attributes

with open("data/user.json") as f:
    for dicts in json.load(f):
        sys.users_list.append(sys.dict_to_userinstance(dicts))

with open("data/admin.json") as f:
    for dicts in json.load(f):
        sys.admin_list.append(sys.dict_to_admininstance(dicts))
    
exit = True
while exit:
    try:
        a = int(input(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\n\tMAIN MENU\n" + Style.RESET_ALL + "=============================\n" +
    "1-  Register User\n"
    "2-  Login\n"
    "3-  Register Admin\n"
    "4-  Exit\n"
    ))
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "Please enter a valid number" + Style.RESET_ALL)

    while True:
        if(a == 1):
            sys.register_user()
            time.sleep(4)
            clear_screen()
            break

        elif(a == 2):
            sys.login()
            time.sleep(4)
            clear_screen()
            break

        elif(a == 3):
            sys.add_admin() 
            time.sleep(4)
            clear_screen()
            break   

        elif(a == 4):
            exit = False 
            break   
        else:
            print("Please enter a valid choice according to menu....")


#writing data collected after running program into it's respective json files

with open("data/user.json", "w") as f:
    dict_list = []
    for user in sys.users_list:
        dict_list.append(sys.instance_to_dict(user))
    json.dump(dict_list, f, indent=4)

with open("data/admin.json", "w") as f:
    dict_list = []
    for admin in sys.admin_list:
        dict_list.append(sys.instance_to_dict(admin))
    json.dump(dict_list, f, indent=4)