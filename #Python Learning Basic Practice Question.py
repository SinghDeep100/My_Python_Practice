#Python Learning Basic Practice Questions %%
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

# %% [markdown]
# 2. Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

# %%
for n in range(0,11):
    #print(n)
    prv_num=n-1
    if n==0:
        print(f"Current Number {n} Previous Number  {n}  Sum:  ",(n))
    else :
        print(f"Current Number {n} Previous Number  {prv_num}  Sum:  ",(n+prv_num))

# %% [markdown]
# 3. Write a Python code to accept a string from the user and display characters present at an even index number.

# %%
str1=input("Type String Value : ")
for n in range(0,len(str1),2):
    print(str1[n])


# %% [markdown]
# 4. Write a Python code to remove characters from a string from 0 to n and return a new string.

# %%
def remove_chars(word, n):
    # write your code
    new_str=word[n:]
    print(new_str)
    

print("Removing characters from a string")
remove_chars("pynative", 4)
# output 'tive' first four characters are removed

remove_chars("pynative", 2)
# output 'native'

# %% [markdown]
# 5. Check if the first and last numbers of a list are the same

# %%
numbers_x = [10, 20, 30, 40, 10]
print(numbers_x[-1]==numbers_x[0])

numbers_y = [75, 65, 35, 75, 30]
print(numbers_y[-1]==numbers_y[0])

# %% [markdown]
# 6. Write a Python code to display numbers from a list divisible by 5

# %%
list1 =  [10, 20, 33, 46, 55]
for n in list1:
    if n%5==0:
        print(n)

# %% [markdown]
# 7. Write a Python code to find how often the substring “Emma” appears in the given string.

# %%
str4 = "Emma is good developer. Emma is a writer"
substr = "Emma"
print(str4)
print(f"{substr} Appeared {str4.count('Emma')} Times.")

# %% [markdown]
# 8. Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# %%
for i in range(1,6):
    for y in range(i):
        print(i,end=" ")
    print()


# %% [markdown]
# Exercise 9: Check Palindrome Number
# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.

# %%
n=12321
nnum=str(12321)
rnum=nnum[::-1]
print(rnum==nnum)

# %% [markdown]
# 10. Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.

# %%
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def merge_list(list1, list2):
    merge = []

    # Append odd numbers from list1
    for num in list1:
        if num % 2 != 0:
            merge.append(num)

    # Append even numbers from list2
    for num in list2:
        if num % 2 == 0:
            merge.append(num)

    print(merge)

merge_list(list1, list2)


