from app.common.database import Database
from app.models.users.errors import UserAlreadyRegistered

class User:
    @classmethod
    def register(cls, data):
        # user = Database.select("""SELECT id FROM user WHERE username = %s""", (data['username'],))
        # if len(user) > 0:
        #     raise UserAlreadyRegistered("User already registered")
        # Database.modify("""INSERT INTO user (username, password) VALUES (%, %)""", (data['username'], data['password']))
        return "usuario registrado"
