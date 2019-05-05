from flask_restful import Resource, reqparse
from app.models.users.user import User as UserModel
from app.models.users.errors import UserAlreadyRegistered


class UserRegister(Resource):
    @classmethod
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help="username is required"
                            )
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help="password is required"
                            )
        data = parser.parse_args()

        try:
            userRegister = UserModel.register(data)
            return {
                "success": True,
                "message": userRegister
            }
        except UserAlreadyRegistered as e:
            return {
                "success": False,
                "message": e.message
            }, 403
