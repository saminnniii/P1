class User:
    def __init__(self,id,name,email):
        self._id=id
        self.name=name
        self.email=email
    def add_to_cart(self,product):
        self.cart.append(product)
    def remove_from_cart(self,product):
        if product in self.cart
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
        self.cart={}
    def add_product(self,product,quantity):
        if product in self.cart:
            quantity+=self.cart[product]
        else:
            self.cart[product]=quantity
    def remove_product(self,product):
        if product in self.cart:
            del self.cart[product]  
        else:
            print("this isnt in tour cart")
    def calculate_total(self):
        total=0  
        for product,quantity in self.cart,items():
            product.price*quantity=+total      
        return total
    def __len__(self):
        return len(self.cart)
    def __str__(self):
        result=""
        for product,quantity in self.cart.items():
            result+=product.name +":"+ str(quantity)+ "\n"
        return result
    def __contains__(self,product):
        if product in self.cart:
            return True
        else:
            return False
class Order:
    def __init__(self,id,user,items,total_price):
        self.id=id
        self.user=user
        self.items=items
        self.total_price=total_price
        self.status=pending
    def pay(self,gateway):
        if self.status=="cancelled":
            return
        gateway.pay(self.total_price)
        self.status="paid"
    def cancel(self):
        if self.status=="paid":
            return
        else:
            self.status="cancelled"
from abc import ABC,abstractmethod
class Paymentgateway(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class Fakepaymentgateway(Paymentgateway):
    def pay(self,amount):
        return "fake payment successful"
class Bankpaymentgateway(Paymentgateway):
    def pay(self,amount):
        return "bank payment successful"







