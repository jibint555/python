#!/usr/bin/python3
def to_upper(data):
    upper_str=''
    for i in data:
        if i.isalpha() and ord(i) in range(97, 123):
             upper_str+=chr(ord(i)-32)
        else:
             upper_str+=i
    return upper_str
'''
function to convert the string into lowercase
'''
def to_lower(data):
    lower_str=''
    for s in data:
        if s.isalpha() and ord(s) in range(65, 91):
            lower_str+=chr(ord(s)+32)
        else:
            lower_str+=s
    return lower_str


def palindrome_check(data):
    cleaned_data=data.replace(" ", "").lower()
    return cleaned_data == cleaned_data[::-1]

if __name__ =='__main__':
     data=input("Enter the string to be converted:\t")
     option=input("choose your option: 1 - > convert to uppercase, 2 - > convert to lowercase, 3 - > is it a palindrome: \t")

     if option == '1':
         output=to_upper(data)
         print(f"\nuppercase of the entered string{data:>10} is {output}")
     elif option == '2':
         output=to_lower(data)
         print(f"\nlowercase of the entered string{data:>10} is {output}")    
     elif option == '3':
         if palindrome_check(data) == True:
        
             print(f"\n{data:>10} is a palindrome")
         else:
             print(f"\n{data:>10} is not a palindrome")
     else:
         print("\nInvalid selection")

