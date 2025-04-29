import math

input = ("Enter transaction type: ")
transaction_type1 = ("Investment - to calculate the amount of interest you will earn on your investment over a period of time")
transaction_type2 = ("Bond - to calculate the amount you will have to pay on a home loan")
print(transaction_type1 + "\n" + transaction_type2 + "\nEnter either 'investment' or 'bond' from the menu below to proceed:")

if not transaction_type1 or not transaction_type2:
     print("You have entered an invalid transaction type" " " "Please enter investement or bond: ")


interest_type1 = ("Simple interest - interest is calculated on the principal amount only")
interest_type2 = ("Compound interest - interest is calculated on the principal amount plus the interest earned in previous periods")
interest = ("interest_type1" or "interest_type2") 


if input == transaction_type1:
    print (str("amount you are depositing" + "\n"  "interest rate" + "\nnumber of years you plan on investing" ))


input = ("Enter type of interest: ")
if input == interest_type1:
    
    P = float(input("Enter the principal amount: "))
    r = float(input("Enter the annual interest rate (as a decimal): "))
    t = int(input("Enter the number of years: "))
    A = P * (1 + r * t)
    
    print(f"Total amount payable after {t} years: {A}")

if input == interest_type2:
        
        P = float(input("Enter the principal amount: "))
        r = float(input("Enter the annual interest rate (as a decimal): "))
        t = int(input("Enter the number of years: "))
        n = int(input("Enter the number of times that interest is compounded per year: "))
        A = P * (1 + r / n) ** (n * t)
        
        print(f"Total amount payable after {t} years: {A}")


if input == transaction_type2:
    print (int("present value of the house" + "\n" "interest rate" + "\nnumber of months you plan on paying the bond" ))

p = int(input("Enter the present value of the house: "))
i = float(input("Enter the annual interest rate (as a decimal): "))
n = int(input("Enter the number of months you plan on paying the bond: ")) 
monthly_amount_payable = (1 * P)/(1 - (1+i)**(-n)) 

print(f"Monthly amount payable: {monthly_amount_payable}")

# The code above is a simple finance calculator that allows the user to calculate either the amount of interest earned on an investment or the monthly payment on a bond.


    








