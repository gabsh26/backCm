from flask_restful import Resource, reqparse
from app.models.users.logout import Logout as LogoutModel


class Logout(Resource):
    
    userLogout = LogoutModel.logout(data)
    return {
                "success": True,
                "message": userLogout
            }
         
       