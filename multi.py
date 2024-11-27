a=[20, 50, 40, 70]
c=0
for i in range(len(a)-1):
    c=(a[i]*a[i+1])
    print(f"The output of condition met at {i}: is  {a[i]}* {a[i+1]} = {c}")

print(f"total: {c}")



