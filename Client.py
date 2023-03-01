class Client:

    limited_number_of_carts = 5 # Temporary field

    def __init__(self,firstname, lastname, phone, email,password, membership) -> None:
        self.firstname=firstname
        self.lastname=lastname
        self.phone=phone
        self.email=email
        self.password = password
        self.membership= membership
        self.carts =[]
        self.orders = []
        
# dataclass