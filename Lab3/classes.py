


"""ex 1"""

"""class ForTwo:
    def __init__(self):
        self.value = ''
    
    def getString(self):
        self.value = input()

    def printString(self):
        print(self.value.upper())
        
example = ForTwo()
example.getString()
example.printString()"""

"""ex 2"""

"""class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        return 0
        
class Square(Shape):
    def __init__(self,length):
        self.length = int(length)
    

    def area(self):
         print(self.length**2)

square = Square(25)
square.area()
"""

"""ex 3"""
"""
class Shape:
    def __init__(self, length):
        self.length = length
        self.shape_area = 0
        

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width
        


    def area(self):
        self.shape_area = self.width * self.length
        print(self.shape_area)

rectangle = Rectangle(2,3)
rectangle.area()
"""

"""ex 4"""

"""import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def show(self):
        print("x :" + str(self.x)  + '\n' + "y :" + str(self.y))


    def move(self, new_x, new_y):       
        self.x = new_x
        self.y = new_y


    def dist(self, second_points):
        self.distance = math.sqrt((self.x - second_points.x) ** 2 + (self.y - second_points.y) ** 2)
        print(self.distance)

points1 = Point(5, 7)
points2 = Point(8, 9)
points1.dist(points2)
"""

"""ex 5"""

"""
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} accepted. New balance: ${self.balance}")
        else:
            print("please give valid amount")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdraw of ${amount} accepted. New balance: ${self.balance}")    
            else:
                print("Ne dostatochno sredstv. Withdrawal denited.")
        else:
            print("Please deposit a valid amount")


account = Account(owner="Akerke", balance=99999999)

account.deposit(10000)
account.withdraw(98760)
"""