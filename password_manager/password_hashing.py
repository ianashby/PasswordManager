import bcrypt

class PasswordHasher:

    def get_hashed_password(self, plain_text_password):
        return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

    def check_password(self, plain_text_password, hashed_password):
        return bcrypt.checkpw(plain_text_password, hashed_password)

