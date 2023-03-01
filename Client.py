class Client:
    def __init__(self,firstname, lastname, phone, email) -> None:
        self.firstname=firstname
        self.lastname=lastname
        self.phone=phone
        self.email=email
        self.cart =[]
        
# dataclass