from product import Product


class Inventory:
    id = 0

    def __init__(self):
        self.id = id
        Inventory.id += 1
        self.products = []

    def additem(self, price, quantity):
        newproduct = Product(price, quantity)
        self.products.append(newproduct)

    def getinentoryvalue(self):
        value = 0
        for product in self.products:
            value += product.getPrice() * product.getQuantity()
        return value

    def amountofproducts(self):
        numberofproducts = 0
        for product in self.products:
            numberofproducts += product.getQuantity()
        return numberofproducts

    def differentproducts(self):
        return len(self.products)


if __name__ == "__main__":
    """
    Create an application which manages an inventory of products. Create a 
    product class which has a price, id, and quantity on hand. Then create 
    an inventory class which keeps track of various products and can sum up 
    the inventory value.
    """
    # create an inventory
    inventory = Inventory()
    # add some products to the inventory
    for i in range(1, 10):
        for j in range(1, 5):
            inventory.additem(i, j)
    # Get amount of product on hand, value of product, and amt of differnet product
    prod_amt = inventory.amountofproducts()
    prod_val = inventory.getinentoryvalue()
    prod_diff = inventory.differentproducts()
    for name, info in (
            ("amount of product", prod_amt), ("value of product", prod_val),
            ("different products", prod_diff)):
        print("{0}: {1}".format(name, info))
