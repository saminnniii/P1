class User:
    def __init__(self,id,name,email):
        self.cart=[]
        self._id=id
        self.name=name
        self.email=email
    def add_to_cart(self,product):
        self.cart.append(product)
    def remove_from_cart(self,product):
        if product in self.cart:
            self.cart.remove(product)
        else:
            print("product is not in cart")
class Product:
    def __init__(self,id,name,price,stock):
        self.id=id
        self.name=name
        self.price=price
        self.stock=stock
    def increase_stock(self,amount):
        if amount<0:
            print("amount must be positive")
            return
        self.stock+=amount
    def decrease_stock(self,amount):
        if amount<0:
            print("amount must be positive")
            return
        if self.stock < amount:
            print("not enough stock")
            return
        self.stock-=amount
class Cart:
    def __init__(self):
        self.cart=[]
        

print(p)



