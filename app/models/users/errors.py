from app.models.base_error import BaseError


class UserAlreadyRegistered(BaseError):
    pass

class IncorrectUser(BaseError):
    pass

class IncorrectPassword(BaseError):
    pass