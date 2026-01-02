import csv
Stock={
    "apple":20,
    "banna":15,
    "orange":30,
    "grapes":50
}
product=input("Enter a product").lower()
quantity=int(input("Enter quntity you need"))
if product in Stock:
    prise=Stock[product]
    total=quantity*prise
    print(f"Total investment is:",total)
else:
    print("Product not in stock Sorry")