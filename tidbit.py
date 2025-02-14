def generate_payment_schedule(purchase_price):
 
    down_payment_rate = 0.10  
    annual_interest_rate = 0.12 
    monthly_payment_rate = 0.05  
    
    down_payment = purchase_price * down_payment_rate
   
    monthly_payment =(purchase_price * monthly_payment_rate)
    
    balance = purchase_price
    month = 1
    
    print(f"{'Month':<10}{'Starting Balance':<20}{'Interest to pay':<20}{'Principal to pay':<20}{'Payment':<20}{'Ending Balance':<20}")
    
    while balance > 0:
       
        Interest_to_pay = balance * (annual_interest_rate / 12)
        
        Principal_to_pay = monthly_payment - Interest_to_pay
        
        if Principal_to_pay > balance:
            Principal_to_pay = balance
        
        balance -= monthly_payment
        
        print(f"{month:<10}{balance + monthly_payment :<20.2f}{Interest_to_pay:<20.2f}{Principal_to_pay:<20.2f}{monthly_payment:<20.2f}{max(0, balance):<20.2f}")
        
        month += 1

purchase_price = float(input("Enter the purchase price: "))
print("\n")
generate_payment_schedule(purchase_price)
