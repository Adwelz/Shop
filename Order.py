from Cart import Cart

class Order:
    def __init__(self,id,client) -> None:
        self.id = id
        self.client = client

    def getPrice(self):
        for cart in self.client.carts:
            sum = 0
            sum+=cart.getCartPrice()
        return sum