from Cart import Cart
from Membership import Membership

class Order:

    def __init__(self,id,client) -> None:
        self.id = id
        self.client = client

    def get_price(self):
        sum = 0
        for cart in self.client.carts:
            sum+=cart.getCartPrice()

        self.client.bonus +=Membership.bonusMembership(sum)
        return sum
    
    def save_order(self):
        self.price = self.get_price()
        self.client.carts = []
        self.client.orders.append(self.id)