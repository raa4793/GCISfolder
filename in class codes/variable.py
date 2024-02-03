"""def add(a,b):
    return (a+b)

def multiply(r,s):
    return (r*s)

a=int(input("enter value 1:"))
b=int(input("enter value 2:"))
addResult=add(a,b)

r=int(input("enter value 3:"))
s=int(input("enter value 4:"))      
multiplyResult=multiply(r,s)

FinalResult=(addResult/multiplyResult)
print(FinalResult)"""

def multiply(x,y):
    return x*y

def subtract(a,b):
    return a-b

def main():
    x=int(input("enter 1:"))
    y=int(input("enter 2:"))
    multiplyResult=multiply(x,y)

    a=6
    b=5
    FinalResult=subtract(multiplyResult,a-b)
    print(FinalResult)


main()