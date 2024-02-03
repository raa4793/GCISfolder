def hello():
    name=input("what is your name?")
    print(name)


hello()


def add(a,b):
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
print(FinalResult)



def main():
    name=input("what is my name?")
    print (name)

main()    