# Exercise 1
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length+self.width)
# Exercise 2
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        return f"{self.title}, Author: {self.author}, Price: ${self.price}"

# Exercise 3
class ShoppingCart:
    lst_price=[]
    lst_name=[]
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def add_item(self,name,price):
        ShoppingCart.lst_name.append(self.name)
        ShoppingCart.lst_price.append(self.price)
    def total_price(self):
        return sum(ShoppingCart.lst_price)
    def show_items(self):
        return ShoppingCart.lst_name
