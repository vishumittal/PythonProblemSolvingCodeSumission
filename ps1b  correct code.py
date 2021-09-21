user_balance=float(input("Enter the outstanding balance on your credit card:"))
intr_rate=float(input("Enter the annual credit card interest rate as a decimal:"))
mon_intr_rate=intr_rate/12.0
min_mon_pay=500
balance= user_balance
months = 1       

while balance>0:
    months=1
    while(months <=12 and balance>0):
        balance= ((balance*(1+mon_intr_rate))-min_mon_pay)
        months += 1
        
        if balance>0:
            min_mon_pay= min_mon_pay+500   
                      
    
print('RESULT:')
print("Monthly payment to pay off debt in 1 year:", min_mon_pay)
print("Number of months needed:",months)
print("Balance: Rs.",round(balance,2))

