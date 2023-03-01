from Cart import Cart
from Membership import Membership

class Order:
    def __init__(self,id,client) -> None:
        self.id = id
        self.client = client

    def getPrice(self):
        for cart in self.client.carts:
            sum = 0
            sum+=cart.getCartPrice()

        if client.membership == True:
            sum = Membership.priceWithMembership(sum)
        return sum