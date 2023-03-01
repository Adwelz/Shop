from Item import Item
from Shop import Shop

class Cart:
    def __init__(self, id, client) -> None:
        self.id = id
        self.client = client
        self.client.carts.append(id)
        self.items = []

    def add2Cart(self,id_item):
        self.items.append(id_item)
        Shop().items[id_item].nbr_left -=1

    def removeOfCart(self, item):
        self.items.remove(item)

    def getCartPrice(self):
        sum = 0
        for item in self.items:
            sum+=item.price
        return sum
    
    def freeship(self):
        if self.client.membership==True:
            freeship_price=10
        else:
            freeship_price=100
        if self.getCartPrice()>freeship_price:
            return True