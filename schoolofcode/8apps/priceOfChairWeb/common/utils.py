from common.general import pbkdf2_sha512, regex
class Utils(object):

    @staticmethod
    def hash_password(password):
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashedPassword):
        """
        :param password: user's provided password
        :param hashedPassword: password in database
        :return: true if 2 passwords match, otherwise False
        """
        return pbkdf2_sha512.verify(password, hashedPassword)

    @staticmethod
    def email_is_valid(email):
        emailAddressMatcher = regex.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if emailAddressMatcher.match(email) else False
