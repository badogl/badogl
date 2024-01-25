import time

# Ask name of the restaurant
restaurant_name=input("What is the restaurant name ? :")
print(f"Welcome to {restaurant_name}\n")
time.sleep(2)

dollar="$"
euro="£"
crreuro=1.09


# Functions Calc to price for meal
def calc_price(a=0,b=0,c=0,d=0,e=0):
    
    # Calc prices
    adu_price=float(a*b)
    chi_price=float(c*d)
    
    # Sub total without tax
    sub_total=adu_price+chi_price
    
    # Show sub total
    print(f"\nSub total is {sub_total}{dollar}\n")
    
    # Calc tax
    conc_tax=sub_total*e
    tax=conc_tax/100
    
    # Show just tax
    print(f"Your tax {round(tax,2)}{dollar}")
    
    # Sum tax and sub_total
    total=sub_total+tax
    print(f"You should pay {round(total,2)}{dollar}\n")
    
    
    
    # Minimum amount the customer can give
    while True:
        
        # Ask for currency
        whatcrr=input("What is the you want pay currency ? :(Euro or Dollar)")
        
        # Make lower string because check on if
        whatcrr=whatcrr.lower()
        
        # Check currency
        if whatcrr == "euro":
            print(f"You need pay {round(total*crreuro,2)}{euro}")
            pay=float(input(f"What is the payment amount ? :"))
            
            # if else blog for check paid amount is more than total
            if pay < total * crreuro:
                print(f"The fee you must pay is at least {round(total*crreuro)}{euro}\n")
                continue
            else:
                print(f"Your change is {round(pay-total*crreuro,3),euro}")
                print("Thank you for your payment!")
                break
        
        
        elif whatcrr == "dollar":
            print(f"You need pay {round(total,2)}{dollar}")
            pay=float(input(f"What is the payment amount ? :"))
            
            # if else blog for check paid amount is more than total
            if pay < total:
                print(f"The fee you must pay is at least {round(total)}{dollar}\n")
                continue
            else:
                print(f"Your change is {round(pay-total,2),dollar}")
                print("Thank you for your payment!")
                break
        break
    
    
    
    

# Ask to customer
price_adult=float(input("The price of a adult's meal ? :(example 1.00) "))
number_adult=int(input("The number of adult ? :(example 1)"))
print("\n")
price_child=float(input("The price of an child's meal ? :(example 1.00)"))
number_child=int(input("The number of children ? :(example 1)"))
print("\n")

# Ask for tax
tax_rate=float(input(f"What is the tax rate ? :(example 1)"))

# Function
calc_price(price_adult,number_adult,price_child,number_child,tax_rate)