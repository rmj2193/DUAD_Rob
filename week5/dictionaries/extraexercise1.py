#Creating dataset with new sales, items, UPCs and prices
sales = [
    {
        "date": "01/03/23",
        "customer_email": "maria@example.com",
        "items": [
            {"name": "Headphones", "upc": "ITEM-101", "unit_price": 120.00},
            {"name": "Notebook", "upc": "ITEM-202", "unit_price": 5.50},
        ],
    },
    {
        "date": "02/03/23",
        "customer_email": "alex@example.com",
        "items": [
            {"name": "Headphones", "upc": "ITEM-101", "unit_price": 115.00},
            {"name": "Backpack", "upc": "ITEM-303", "unit_price": 45.99},
        ],
    },
    {
        "date": "02/03/23",
        "customer_email": "sofia@example.com",
        "items": [
            {"name": "Notebook", "upc": "ITEM-202", "unit_price": 6.00},
            {"name": "Pen", "upc": "ITEM-404", "unit_price": 1.25},
        ],
    },
    {
        "date": "03/03/23",
        "customer_email": "liam@example.com",
        "items": [
            {"name": "Backpack", "upc": "ITEM-303", "unit_price": 42.50},
            {"name": "Pen", "upc": "ITEM-404", "unit_price": 1.10},
        ],
    },
]

# Dictionary to store total sales for each UPC
sales_totals = {}

# Loop through each sale in the list
for sale in sales:
    # Loop through each item inside the current sale
    for item in sale["items"]:
        upc = item["upc"]              # Unique product code
        price = item["unit_price"]     # Price of this sale for that item

        # If we haven't seen this UPC yet, initialize it with 0.0
        if upc not in sales_totals:
            sales_totals[upc] = 0.0
        
        # Add the item's price to the total for this UPC
        sales_totals[upc] += round(price, 2)

# Print the final totals for each UPC
print(sales_totals)