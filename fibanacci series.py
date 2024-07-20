n = int(input("enter the number: "))
a=0
b=1
count = 0
if n <= 0:
    print("check the entered value again")
elif n == 1:
    print(a)
else:
    print("fibonacci series:")
    while count < n:
        print(a)
        v = a + b
        a = b
        b = v
        count += 1
