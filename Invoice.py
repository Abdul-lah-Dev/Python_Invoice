# invoice.py Microlab B Python Basics
#Calculate invoice total with correct data types and f-strings

print("===Invoice Generator===")


#1. Ask user for input of the data
item_name= input("Enter the name of Item: ")
input_quantity= input("Enter the quantity: ")
input_unit_price= input("Enter the unit price of the item ($): ")

#2. Link inputs to proper data types
quantity=int(input_quantity)
unit_price=float(input_unit_price)


#3. Calculation of total price

total_amount = quantity * unit_price

print("\n" + "="*25)
print(f"ITEM: {item_name}")
print(f"Quantity: {input_quantity}")
print(f"Unite Price: ${unit_price:.2f}")
print("-"*25)
print(f"Total Price: ${total_amount:.2f}")
print("="*25)

