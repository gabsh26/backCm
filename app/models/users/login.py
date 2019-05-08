from app.common.database import Database

class Login:
    @classmethod
    def login(cls, data):
        # user = Database.select("""SELECT id FROM user WHERE username = %s""", (data['username'],))
        # if len(user) > 0:
        #     raise UserAlreadyRegistered("User already registered")
        # Database.modify("""INSERT INTO user (username, password) VALUES (%, %)""", (data['username'], data['password']))
        return "registro exitoso"
