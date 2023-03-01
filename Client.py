class Client:
    def __init__(self,firstname, lastname, phone, email) -> None:
        self.firstname=firstname
        self.lastname=lastname
        self.phone=phone
        self.email=email
        self.favorite_color = favorite_color #
        self.carts =[]
        self.bonus = 0 

    def printInfo(self):
        print("firstname: " + self.firstname)
        print("lastname:" + self.lastname)
        print("phone:" + self.phone)
        print("email:" + self.email)
        print("carts:" + self.carts)
        print("bonus:" + self.bonus)