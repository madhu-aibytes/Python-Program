def string_reverse_with_recursion(s):
    rev = ""
    for i in range(len(s)):
        rev = s[i] + rev
    print(rev)
s = input("Enter a string to reverse: ")
string_reverse_with_recursion(s)

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






'''def string_reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + string_reverse_with_recursion(s[:-1])
input_string = input("Enter a string to reverse: ")
reversed_string = string_reverse_with_recursion(input_string)
print(f"The reversed string is: {reversed_string}")
# This code defines a recursive function to reverse a given string.'''