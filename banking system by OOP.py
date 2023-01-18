# parent class
class user:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("personal Details---")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Gender : ", self.gender)
# child class


class bank(user):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def balences(self):
        print("balances are: ", self.balance)

    def deposits(self, amount):
        if amount > 499:
            self.balance = self.balance + amount
            print("The amount are successfully Deposited!")
        else:
            print("Deposits less than 500 is not permitted")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balances| your balance are: ", self.balance)
        else:
            self.balance = self.balance - amount
            print("the amount are successfully withdrawed")

    def view_details(self):
        super().show_details()
        print("your balence is : ", self.balance)


# //////////////////////////////////////////////////////////////////////////////////////////
customer1 = bank("safaith", 24, "Male")
customer2 = bank("kutub", 26, "Male")

customer1.deposits(100)
customer1.deposits(500)
# customer2.deposits(1000)
# customer1.withdraw(200)

customer1.view_details()
# customer2.view_details()
