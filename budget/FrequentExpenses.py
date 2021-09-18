from . import Expense
import collections

expenses=Expense.Expenses()
# print(expenses)
expenses.read_expenses('data/spending_data.csv')


spending_categories=[]
# print(expenses.category)
# For loop over expense list, to append spending list with each category
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter=collections.Counter(spending_categories)
top5=spending_counter.most_common(5)
print(top5)