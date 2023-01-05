#program for armstrong number
n=int(input("Enter Number:\n"))
on=n 
an=0
while n>0:
    r=n%10
    c=r**3
    an=an+c 
    n=n//10
if an==on:
    print(on,"is a armstrong number", on, "and", an, "is same")
else:
    print(on,"is not a armstrong number", on, "and", an, "is not same")
