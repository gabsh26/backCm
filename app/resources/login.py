from flask_restful import Resource, reqparse
from app.models.users.user import Login as LoginModel
from app.models.users.errors import IncorrectUser
from app.models.users.errors import IncorrectPassword

class Login(Resource):
    @classmethod
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help="Incorrect username"
                            )
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help="Incorrect password"
                            )
        data = parser.parse_args()

        try:
            userLogin = LoginModel.login(data)
            return {
                "success": True,
                "message": userLogin
            }
        except IncorrectUser as e:
            return {
                "success": False,
                "message": e.message
            }, 403

        except IncorrectPassword as e:
            return {
                "success": False,
                "message": e.message
            }, 403