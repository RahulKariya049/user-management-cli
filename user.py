class user:
    def __init__(self, name : str, email : str, password : str) -> None:
        self.name = name
        self._email = email
        self.__password = password

    def get_profile(self) -> None:
        print(f"[USER] {self.name}\nEmail Address: {self._email}\n")

    @property
    def email(self) -> str:
        return self._email
    
    def check_password(self, string : str) -> bool:
        return self.__password == string
    
    def change_password(self, new : str) -> None:
        self.__password = new

    @staticmethod
    def dashboard():
        return("\n==================="
        "    USER DASHBOARD\n"
        "===================\n"
        "1. Change Password\n"
        "2. Show Email\n"
        "3. Show Profile\n"
        "4. Logout\n")

    def get_password(self) -> str:
        return self.__password
    