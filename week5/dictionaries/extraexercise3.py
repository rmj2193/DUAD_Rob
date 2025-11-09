#Creating Product dataset
products = [
    {"name": "Monitor", "category": "Electronics", "price": 200},
    {"name": "Keyboard", "category": "Electronics", "price": 50},
    {"name": "Chair", "category": "Furniture", "price": 120},
    {"name": "Table", "category": "Furniture", "price": 180},
    {"name": "Mouse", "category": "Electronics", "price": 25},
]

#Empty dictionary to store the total price for each category
totals_by_category = {}

#Loop through each product in the list
for product in products:
    category = product["category"]  #Get the category of the product
    price = product["price"]        #Get the price of the product
    
    #If this category is not yet in the dictionary, start with 0
    if category not in totals_by_category:
        totals_by_category[category] = 0
    
    #Add the product's price to the correct category
    totals_by_category[category] += price

#Print the result
print(totals_by_category)