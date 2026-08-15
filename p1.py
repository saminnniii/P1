def log_action(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        if func.__name__ == "add_to_cart":
             print("product added successfully")
        elif func.__name__ == "remove_from_cart":
             print("product removed successfully")
    return wrapper
class User:
    def __init__(self,id,name,email,cart):
        self._id=id
        self.name=name
        self.email=email
        self.cart=cart
    @log_action
    def add_to_cart(self,product,quantity):
        self.cart.add_product(product,quantity)
    @log_action
    def remove_from_cart(self,product,quantity):
        self.cart.remove_product(product,quantity)
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
    @classmethod
    def from_dict(cls,data):
        return cls(data["id"], data["name"], data["price"], data["stock"])
    @staticmethod
    def is_valid_price(value):
        if value>0 :
            return True
        else:
            return False
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
        for product,quantity in self.cart.items():
            total += product.price * quantity      
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
    def __init__(self,id,user,items,total_price,cart,Paymentgateway):
        self.id=id
        self.user=user
        self.items=items
        self.total_price=total_price
        self.cart=cart
        self.Paymentgateway=Paymentgateway
        self.status="pending"
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
class EmailNotification:
    def send(self,message):
        print("Email sent")
class SMSNotification:
    def send(self,message):
        print("SMS sent")
def notify_user(notification,message):
    notification.send(message)
class OrderTransaction:
    def __enter__(self):
        print("Transaction started")
    def __exit__(self,exc_type,exc_value,traceback):
        print("Transaction finished")
        if exc_type==None:
            print("no error")
        else:
            print("error found")
with OrderTransaction():
    print("Creating order...")
class Orderservice:
    def __init__(self,product_repository):
        self.product_repository=product_repository
    def create_order(self,id, user, items, total_price, cart, gateway):
        return Order(id, user, items, total_price, cart, gateway)
    def pay_order(self,order,gateway):
        order.pay(gateway)
    def cancel_order(self,order):
        order.cancel()
class productrepository:
    def __init__(self):
        self.products=[]
    def add(self,product):
        self.products.append(product)
    def get_by_id(self,id):
        for product in self.products:
            if product.id == id :
                return product
    def get_all(self):
        return self.products
    def delete(self,id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
cart = Cart()

user = User(1, "Samin", "samin@gmail.com", cart)
product1 = Product(1, "Laptop", 50000, 10)
product2 = Product(2, "Mouse", 2000, 20)
product3 = Product(3, "Keyboard", 3000, 15)
repository = productrepository()
repository.add(product1)
repository.add(product2)
repository.add(product3)
user.add_to_cart(product1, 1)
user.add_to_cart(product2, 2)
print(cart)
total = cart.calculate_total()
print("Total price:", total)
gateway = Fakepaymentgateway()
service = Orderservice(repository)
order = service.create_order(1,user,cart.cart,total,cart,gateway)
service.pay_order(order, gateway)
product1.stock -= 1
product2.stock -= 2
notification = EmailNotification()
notify_user(notification,"Your order has been paid successfully.")
print("Final order status:", order.status)

















