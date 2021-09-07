# Problem Set 1a
# Name: Vaishnavi Mittal
# Time Spent: 2:00

p=float(input("Enter the outstanding balance on your credit card:"))
ann_intr=float(input("Enter the annual credit card interest rate as a decimal:"))
min_mon_payrate=float(input("Enter the minimum monthly payment rate as a decimal:"))
bal = p
       
result = 0
for i in range(1,13):
    min_mon_pay = bal*min_mon_payrate
    intr_paid = (ann_intr/12) * bal
    ppl_paid = min_mon_pay- intr_paid 
    remain_bal= round(bal- ppl_paid,2)
    print("Month:",i)
    print("Minimum monthly payment:", min_mon_pay)
    print("Principal paid:",round(ppl_paid,2))
    print("Remaining balance:", round(remain_bal,2))
    result = result + min_mon_pay
    bal = remain_bal
print('RESULT:')
print("Total amount paid:", result)
print("Remaining balance:",bal)
