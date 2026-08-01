

def spacer():
    for i in range(100):
        print("\n")

spacer()

print("Welcome to Neil's Bakery")
print()

menu = ["Milkshake", "Ice Cream", "Chocolate", "Eclairs ", "CupCake ", "Dounut  ", "Cheese Cake", "Sundae  " ]
price = [ 5.00, 3.00, 2.00, 2.00, 1.00, 2.00, 5.00, 8.00]

print("ITEM", "PRICE (USD), excl. Tax", sep="\t\t")
for kk in range(len(menu)):
    print(str(kk+1)+". "+menu[kk], price[kk], sep="\t\t")

shopping_cart = [] 
shopping_quant= []
shopping_complete = 0

while shopping_complete==0:

    order = int(input("Enter 1 to 8 to select an item or enter 9 to proceed to checkout.\n")) 
    
   
    
    if order <= 8:
        print("You selected", menu[order-1])
        quant = int(input("How many units do you wish to purchase?\n"))

        if menu[order-1] in shopping_cart:
            idx = shopping_cart.index(menu[order-1])
            shopping_quant[idx]+=quant
        else:
            shopping_cart.append(menu[order-1])        
            shopping_quant.append(quant)        
        
        print("Added ", quant," " ,menu[order-1] ,"(s) to your shopping cart :)", sep="" )
    elif order == 9:
        shopping_complete = 1
    else: 
        print("ERROR! . ERROR! . ERROR! that was not a valid input plz try again.")

print()
print("shopping cart:")

grand_tot = 0.0
print("ITEM", "QUANT", "UNIT PRICE", "TOTAL", sep="\t\t")    
for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price=price[idx]
    tot_price = round(unit_price*shopping_quant[kk], 2)
    grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep="\t\t")

grand_tot = round(grand_tot, 2)
print()
print("Your total order is (USD)", grand_tot)

next_50 = 50*(grand_tot//50+1)
gap_50 = next_50 - grand_tot


print ("if u purchace for ", next_50," u get a 10% discount")
discount_wanted = input("would u like this offer yn")

add_quant = []

dct_rate = 10.0;
tax_rate = 3.0;

if discount_wanted == 'y':
    #discount = round(dct_rate/100.0*grand_tot, 2)
    print ("here are the following options")
    for i in range(len(menu)):
        add_quant.append(int(gap_50//price[i]+1))
        
        print(str(i+1), ".add", menu[i], "\t\t", add_quant[i], "units")

    add_on = int(input("plz indicate your prefrance\n"))

    if menu[add_on-1] in shopping_cart:
                idx = shopping_cart.index(menu[add_on-1])
                shopping_quant[idx] = shopping_quant[idx] + add_quant[add_on-1]
    else:
        shopping_cart.append(menu[add_on-1])        
        shopping_quant.append(add_quant[add_on-1])        
else:
    discount = 0.0; 


print()
print("shopping cart:")

grand_tot = 0.0
print("ITEM", "QUANT", "UNIT PRICE", "TOTAL", sep="\t\t")    
for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price=price[idx]
    tot_price = round(unit_price*shopping_quant[kk], 2)
    grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep="\t\t")

grand_tot = round(grand_tot, 2)
print()
print("Your total order is (USD)", grand_tot)