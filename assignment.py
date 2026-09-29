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
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price}"

# Exercise 3
class ShoppingCart:
    lst_price=[]
    lst_name=[]
    result=''
    def __init__(self):
        pass
    def add_item(self,name,price):
        ShoppingCart.lst_name.append(name)
        ShoppingCart.lst_price.append(price)
    def total_price(self):
        return sum(ShoppingCart.lst_price)
    def show_items(self):
        for i in range(len(ShoppingCart.lst_name)-1):
            ShoppingCart.result += f"{ShoppingCart.lst_name[i]}: ${ShoppingCart.lst_price[i]}\n"
        ShoppingCart.result += f"{ShoppingCart.lst_name[i]}: ${ShoppingCart.lst_price[i]}"
        return ShoppingCart.result
