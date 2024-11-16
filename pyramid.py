#!/usr/bin/python3
rows=int(input("enter number of rows: \t"))
for i in range(1, rows+1):
    print(" " * (rows-i),end=" ")
    print("*" * (3 * i - 1))


