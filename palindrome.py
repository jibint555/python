#!/usr/bin/python3
string=input("Enter the string : \t")
cleaned_string=string.replace(" ", "").lower()
if cleaned_string == cleaned_string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")

