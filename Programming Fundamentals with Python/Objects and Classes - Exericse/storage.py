class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):
        if self.capacity > 0:
            Storage.storage.append(product)
            self.capacity -= 1

    def get_products(self):

        return Storage.storage


storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
storage1 = Storage(5)
storage1.add_product("apple")
storage1.add_product("banana")
storage1.add_product("potato")
storage1.add_product("tomato")
storage1.add_product("bread")
print(storage.get_products())
