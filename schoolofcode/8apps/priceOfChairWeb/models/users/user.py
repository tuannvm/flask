''' user model '''
from common.utils import Utils
from common.database import Database
from common.general import uuid4
from common.errors import UserNotExistsError, UserIncorrectPasswordError, UserEmailInvalid, UserExistsError
import constants


class User(object):
    ''' User class '''
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid4().hex if _id is None else _id

    def __repr__(self):
        return "show user {} with password".format(self.email)

    @staticmethod
    def login_valid_user(email, password):
        """
        :param  email: user's email
        :param password: user's password
        :return: True if valid, False otherwise
        """
        userData = Database.find_one("users", {'email': email})
        if userData is None:
            raise UserNotExistsError("this user does not existed!")
            return False
        if not Utils.check_hashed_password(password, userData['password']):
            raise UserIncorrectPasswordError("Incorrect password!")
            return False
        return True

    @staticmethod
    def register_user(email, password):
        """
        This method registers a user using  e-mail and password.
        The password already come with sha-512 hash algorithm.
        :param email: user's email (might be invalid)
        :param password: sha512-hashed password
        :return: True if registered successfully, of False otherwise
        """
        userData = Database.find_one("users", {'email': email})
        if userData is not None:
            raise UserExistsError("user already existed!")
        #if email is invalid, then what?
        if not Utils.email_is_valid(email):
            raise UserEmailInvalid("invalid email!")
        #hash password, create new object, then insert to db
        User(email, Utils.hash_password(password)).save_to_db()
        return True

    def save_to_db(self):
        Database.insert(constants.COLLECTION, self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }
