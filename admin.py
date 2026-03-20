from user import user

class admin(user):

    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
    
    @staticmethod
    def dashboard() -> None:
        return (
    "\nAdmin Dashboard\n"
    "=================\n"
    "1. View all users\n"
    "2. Show my profile\n"
    "3. Reset Password\n"
    "4. Logout\n")


    def get_profile(self) -> str:
        print( f"[Admin] {self.name} | {self.email}")

    