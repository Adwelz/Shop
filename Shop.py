from Item import Item

class Shop:

    def __init__(self) -> None:
        self.name = "Carrefour"
        self.director = "Bernard"
        self.director_id = 1
        self.director_phone = 0830095075
        self.manager = "Claude"
        self.manager_id =2
        self.manager_phone = 0830095076
        self.items = []
        self.items.append(Item(0,6,8))
        self.items.append(Item(1,5,9))
        self.items.append(Item(2,2,11))
        self.items.append(Item(3,9,14))

# dataclass