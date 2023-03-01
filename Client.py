class Client:
    def __init__(self,firstname, lastname, phone, email, membership) -> None:
        self.firstname=firstname
        self.lastname=lastname
        self.phone=phone
        self.email=email
        self.membership= membership
        self.carts =[]
        self.orders = []
        
# dataclass