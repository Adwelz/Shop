from Item import Item

class Cart:
    def __init__(self, id, client) -> None:
        self.id = id
        self.client = client
        self.client.carts.append(self)
        self.items = []

    def add2Cart(self,item):
        self.items.append(item)

    def removeOfCart(self, item):
        self.items.remove(item)

    def getCartPrice(self):
        sum = 0
        for item in self.items:
            sum+=item.price
        return sum