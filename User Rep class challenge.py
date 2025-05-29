class UserRep:
    def __int__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = False
        self.login_attempts = 0


    def deactivate(self):
        self.is_active = False

    def rest_login_attempts(self):
        self.login_attempts = 0

    def show_profile(self):
        print(self.username)
        print(self.email)
        print(self.is_active)
        print(self.login_attempts)