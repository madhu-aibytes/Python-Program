def reverse_integer(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
n = int(input("Enter a positive integer to reverse: "))
reversed_integer = reverse_integer(n)
print(f"The reversed integer is: {reversed_integer}")