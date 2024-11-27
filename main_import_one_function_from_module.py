#/usr/bin/python3
from stringoperations import to_upper
from stringoperations import to_lower
data=input("enter the string: \t")
option=int(input("Enter the option 1 - > uppercase, 2 - > lowercase, 3 - > palindrome : \t"))


if option == 1:
   output=to_upper(data)
   print(f"\n uppercase of {data:<10} is {output}")
elif option == 2:
   output=to_lower(data)
   print(f"\n lowercase of {data:<10} is {output}")
elif option == 3:
   if palindrome_check(data) == True:
       print(f"\n {data} is a palindrome")
   else:
        print(f"\n {data} is not a palindrome")
else:
   print("wrong option selection")

