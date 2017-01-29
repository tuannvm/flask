class UserError(Exception):
    def __init__(self, message):
        self.message = message

class UserNotExistsError(UserError):
    pass

class UserIncorrectPasswordError(UserError):
    pass

class UserExistsError(UserError):
    pass

class UserEmailInvalid(UserError):
    pass
