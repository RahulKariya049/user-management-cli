from user import user
from admin import admin
from utilities import my_print

class system:
    users_list = []
    admin_list = []
    def register_user(self) -> None:
        name = input("Please enter your Name: ")
        email = input("Please enter your Email: ")
        password = input("Please enter your password: ")

        #create an instance of user 
        user_temp = user(name, email, password)
        
        my_print("\nUser Registered Succesfully.....\n", "GREEN")
        user_temp.get_profile()
        self.users_list.append(user_temp)

    def add_admin(self):
        name = input("Please enter your Name: ")
        email = input("Please enter your Email: ")
        password = input("Please enter your password: ")

        #create an instance of Admin 
        admin_temp = admin(name, email, password)
        
        my_print("\nAdmin Registered Succesfully.....\n" , "GREEN")
        admin_temp.get_profile()
        self.admin_list.append(admin_temp)

    def login(self) -> None:
        handle = input("Enter your Username or Email:\n")
        pin = input("Enter your password:\n")

        # Try user login
        for user_obj in self.users_list:
            if (handle == user_obj.name or handle == user_obj.email) and user_obj.check_password(pin):
                my_print("\n✅ Successfully Logged in as User!", "GREEN")
                self.user_dashboard(user_obj)
                return

        # Try admin login
        for admin_obj in self.admin_list:
            if (handle == admin_obj.name or handle == admin_obj.email) and admin_obj.check_password(pin):
                print("\n✅ Successfully Logged in as Admin!")
                self.admin_dashboard(admin_obj)
                return

        my_print("❌ Invalid username or password." , "RED")
    
    @staticmethod
    def user_dashboard(user_obj) -> None:
        exit = True
        while(exit):
            while True:
                my_print("\nUser Dashboard", "CYAN", True)
                print(user_obj.dashboard())

                choice = input("Enter your choice: ")

                if choice == "1":
                    new_pass = input("Enter your new password: ")
                    user_obj.change_password(new_pass)
                    my_print("✅ Password changed successfully.", "GREEN")
                elif choice == "2":
                    print(f"📧 Email: {user_obj.email}")
                elif choice == "3":
                    user_obj.get_profile()
                elif choice == "4":
                    print("👋 Logging out...")
                    exit = False
                    break
                else:
                    print("⚠️ Invalid choice. Try again.")


    @staticmethod
    def admin_dashboard(admin_obj) -> None:
        exit = True
        while(exit):
            while True:
                my_print("\nAdmin Dashboard", "MAGENTA", True)
                print(admin_obj.dashboard())

                choice = input("Enter your choice: ")

                if choice == "1":
                    print("\n📋 Registered Users:")
                    for i, user in enumerate(system.users_list, 1):
                        print(f"{i}. {user.name} | {user.email}")
                elif choice == "2":
                    admin_obj.get_profile()
                elif choice == "3":
                    username = input("Enter the username whose password you want to reset: ")
                    system.reset_password(username)
                elif choice == "4":
                    print("👋 Logging out...")
                    exit = False
                    break
                else:
                    print("⚠️ Invalid choice. Try again.")
    

    @staticmethod
    def view_users():
        print("\nRegistered Users:")
        for i, user in enumerate(system.users_list, 1):
            print(f"{i}. {user.name} | {user.email}")


    @staticmethod
    def reset_password(username) -> None:
        for user in system.users_list:
            if user.name == username:
                new_password = input(f"Enter new password for {username}: ")
                user.change_password(new_password)
                my_print("✅ Password reset successfully.", "GREEN")
                return
        print("❌ User not found.")

    @staticmethod
    def dict_to_userinstance(dict) -> object:
        return user(dict.get('name'), dict.get('email'), dict.get('password'))
    
    @staticmethod
    def dict_to_admininstance(dict) -> object:
        return admin(dict.get('name'), dict.get('email'), dict.get('password'))

    @staticmethod
    def instance_to_dict(obj) -> dict:
        return {
        'name' : obj.name,
        'email' : obj._email,
        'password' : obj.get_password()
        }
