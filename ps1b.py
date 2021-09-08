


# Problem Set 1b
# Name: Vaishnavi Mittal
# Time Spent: 5:00:00(still i am not able to get to the correct answer)

balance=float(input("Enter the outstanding balance on your credit card:"))
intr_rate=float(input("Enter the annual credit card interest rate as a decimal:"))
mon_intr_rate=intr_rate/12.0
min_mon_pay=500
months = 0       

while balance >0:
    months=0
    prev_bal= balance
    min_mon_pay= min_mon_pay+500                
    while(months <=12 and balance>0):
        balance= ((prev_bal*(1+mon_intr_rate))-min_mon_pay)
        months += 1

       

print('RESULT:')
print("Monthly payment to pay off debt in 1 year:", min_mon_pay)
print("Number of months needed: ",months)
print("Balance: Rs.",round(min_mon_pay,2))
