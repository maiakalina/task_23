menu = ['latte', 'açai bowl', 'banana bread', 'avocado on toast']
stock = {'latte': 78,
         'açai bowl': 8,
         'banana bread': 7,
         'avocado on toast': 9
         }
price = {'latte': 3.5,
         'açai bowl': 9,
         'banana bread': 5.5,
         'avocado on toast': 9.5
         } # #inflation

total_stock_worth = 0

# Looping through the menu items to calculate the total stock value
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value
print(total_stock_worth)