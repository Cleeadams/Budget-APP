import math


class Category:
    astricts = {'Food': '*************', 'Clothing': '***********', 'Entertainment': '********'}

    # Creates or intiates the object!
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.spent = float(0)
        self.proportion = float(0)

    def get_ast(self):
        return Category.astricts[self.name]

    def deposit(self, amount, description=None):
        self.ledger.append(float(amount))
        self.ledger.append(description)

    def withdraw(self, amount, description=None):
        if self.check_funds(amount) == True:
            self.ledger.append(float(-amount))
            self.ledger.append(description)
            self.spent += float(amount)
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

def create_spend_chart(categories):
    total = float(0)
    maxPercent = 100
    output = ''
    for object in categories:
        total += round(object.spent,2)

    for object in categories:
        object.proportion = math.floor(object.spent/total*100)
    print('Percentage spent by category')
    for i in range(11):
        objectCharc = ''
        for object in categories:
            if object.proportion >= maxPercent:
                objectCharc += 'o  '
            else:
                objectCharc += '   '
        output += f'{maxPercent:3}| ' + objectCharc + '\n'
        maxPercent -= 10
    blank = ''
    blankSize = 3*len(categories) + 1
    output += f'    {blank:-^{blankSize}}\n'

    maxNameLen = 0
    for object in categories:
        if len(list(object.name)) > maxNameLen:
            maxNameLen = len(list(object.name))

    for i in range(maxNameLen):
        output += '     '
        for object in categories:
            if len(list(object.name)) < i+1:
                output += '   '
            else:
                output += f'{list(object.name)[i]}  '
        output += '\n'

    return output
