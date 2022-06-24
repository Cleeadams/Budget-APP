import budget
from budget import create_spend_chart


food = budget.Category('Food')
food.deposit(400, 'monthly food budget')
food.withdraw(3, 'lunch')

clothing = budget.Category('Clothing')
clothing.deposit(400, 'monthly lothing budget')
clothing.withdraw(3, 'lunch')

print(food)
print(create_spend_chart([food,clothing]))






