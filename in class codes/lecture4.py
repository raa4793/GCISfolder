#methods to return:
def add(a,b):
    return a+b

def subtract(x,y):
    return x-y


def main():
    a= int(input("enter value 1:"))
    b= int(input("enter value 2:"))
    addResult=add(a,b) #this result will receive the addidtion
    
    x=int(input("enter value 3:"))
    y=int(input("enter value 4:"))

    FinalResult=subtract(addResult,x-y)
    print(FinalResult)

main()