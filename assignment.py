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
    def __init__(self):
        self.lst_price=[]
        self.lst_name=[]
        self.result=""
    def add_item(self,name,price):
        self.lst_name.append(name)
        self.lst_price.append(price)
    def total_price(self):
        return sum(self.lst_price)
    def show_items(self):
        for i in range(len(self.lst_name)-1):
            self.result += f"{self.lst_name[i]}: ${self.lst_price[i]}\n"
        self.result += f"{self.lst_name[len(self.lst_price)-1]}: ${self.lst_price[len(self.lst_price)-1]}"
        return self.result
