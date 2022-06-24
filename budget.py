
class Category:
    astricts = {'Food': '*************', 'Clothing': '***********', 'Entertainment': '********'}

    # Creates or intiates the object!
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def get_ast(self):
        return Category.astricts[self.name]

    def deposit(self, amount, description=None):
        self.ledger.append(float(amount))
        self.ledger.append(description)

    def withdraw(self, amount, description=None):
        if self.check_funds(amount) == True:
            self.ledger.append(float(-amount))
            self.ledger.append(description)
            return True
        else:
            False

    def get_balance(self):
        amount = float(0)
        for i in self.ledger:
            if isinstance(i, float):
                amount = amount + i
        return amount

    def transfer(self, amount, arg):
        if self.check_funds(amount) == True:
            self.withdraw(amount, 'Tranfer to '+arg.name)
            arg.deposit(amount, 'Transfer from '+self.name)

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __repr__(self):
        amnt = []
        descrip = []
        items = ''
        print(f'{self.name:*^30}')
        for i in self.ledger:
            if isinstance(i, float):
                amnt.append(i)
            elif i == None:
                descrip.append('')
            else:
                descrip.append(i)

        for i in range(len(amnt)):
            items += f'{descrip[i][0:23]:23}' + f'{amnt[i]:7.2f}\n'
        output = items + 'Total: ' + str(self.get_balance())
        return output

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(auto)
print(clothing)
print(food)

