print("This Section is for all the Basic level Practice questions Topic Wise")
#---------------------------------------------------------------------------------------------------
## ================================CALCULATE THE PRODUCT AND SUM OF TWO NUMBERS ===============================================
#Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
num1,num2=20,70
prod = num1*num2
if prod<=1000:
    print(f"Product of {num1} and {num2} is {prod}.")
else :
    print(f"Sum of {num1} and {num2} is ",(num1+num2))
