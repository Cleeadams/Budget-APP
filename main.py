from budget import *
from budget import create_spend_chart


food = Category('Food')
food.deposit(900, "deposit")
entertainment = Category('Entertainment')
entertainment.deposit(900, "deposit")
business = Category('Business')
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)


print(create_spend_chart([business,food,entertainment]))
print(food)





