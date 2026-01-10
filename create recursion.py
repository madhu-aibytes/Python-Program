'''n=int(input("Enter a positive integer to calculate sum of digits: "))
sum_digits = 0
if n ==0:
    sum_digits = 0
while n > 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10
print(f"The sum of the digits is: {sum_digits}")'''

def recursion(n):
    if n <= 0:
        return 0
    else:
        return n + recursion(n - 1)
n=int(input("Enter a positive integer: "))
result = recursion(n)
print(f"The sum of first {n} natural numbers is: {result}")



'''def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
n = int(input("Enter a positive integer to calculate sum of digits: "))
result = sum_of_digits(n)
print(f"The sum of the digits is: {result}")'''



    
    
