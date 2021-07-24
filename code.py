import os
print('You are the seller, through this program you will add your products and their price.')

list_of_products = []
products = dict()

def check_if_number(num):
    try:
        num = int(num)
        return num
    except ValueError:
        try:
            num = float(num)
            return num
        except ValueError:
            pass        

while True:
    product = str(input('Product is name: ')).strip().title()
    while True:
        price = check_if_number(input('Price of product: U$'))
        if price is None:
            print('Price not accepted, please enter a valid value.')
        else:
            break
    products['product'] = product
    products['price'] = price
    product = ''
    price = 0
    list_of_products.append(products)
    products = dict()
    print(list_of_products)
    follow_or_not = str(input('Do you want to add another product?')).strip().lower()[0]
    if follow_or_not == 'n':
        break
    os.system('clear')      
cont = 0
for p in list_of_products:
    new = [p['price'] for p in list_of_products]
total = sum(new)
averange = total / len(new)
i=0
print(new)   
maior = list_of_products[new.index(max(new))]
os.system('clear')  
print(f"The most expensive product is the {maior['product']}, and it costs U${maior['price']}")
print(f'All products together cost U$ {total}')
print(f'Average price: U${averange}')