class Connexion:
    def __init__(self) -> None:
        pass

    def verify_password(self, user,typed_password):
        if typed_password == user.password:
            return True
        return False