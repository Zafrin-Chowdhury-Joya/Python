string = input("Enter a number: ").lower()

reversed_string = string[::-1]#string slicing

print(string, reversed_string)

result = "Palindrome" if string == reversed_string else "Not Palindrome"#ternary operator

print(result)

