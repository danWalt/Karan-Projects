

class Product:
    id = 0

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
        self.id = id
        Product.id += 1

    def setPrice(self, newprice):
        self.price = newprice

    def setID(self, newID):
        self.id = newID

    def setQuantity(self, newQuantity):
        self.quantity = newQuantity

    def getPrice(self):
        return self.price

    def getID(self):
        return self.id

    def getQuantity(self):
        return self.quantity
