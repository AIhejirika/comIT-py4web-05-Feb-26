# Operator Overloading
# Arithmetic: + (__add__), - (__sub__), * (__mul__), / (__truediv__)
# Comparison: == (__eq__), != (__ne__), < (__lt__), > (__gt__)

class Product:
    
    # constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # Operator(s) overloading
    def __add__(self, other): # +
        #return self.price + other.price
        if isinstance(other, Product):
            return Product(f"{self.name}+{other.name}", self.price + other.price)
        return Product("Total", self.price + other)
    
    def __radd__(self, other):
        if other == 0:
            return self
        return self.__add__()
    
    def __mul__(self, number):
        return Product(f"{number} {self.name}s", self.price * number)
    
    # CLI represention 
    def __str__(self):
        """user friendly"""
        return f"{self.name}: ${self.price}"
    
    def __repr__(self):
        """developer friendly"""
        return self.__str__()

apple = Product("apple", 2.55)
orange = Product("orange", 1.88)
chips = Product("lays", 4.99)

print(apple, orange)
print(apple + orange*26 + chips)

cart = []
cart.append(apple*3)
cart.append(orange*2)
cart.append(chips*5)

print(cart)
print("Total in Cart: ", sum(cart))




    