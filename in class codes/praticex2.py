def fun(a,b):
    x=a+b
    return x


z=fun(3,5)
print(z)




def multiple(n1,n2):
    result= n1*n2
    print("the multiple is", result)


n1=4
n2=9
multiple(n1,n2)


def multiple(n1,n2):
    y= n1*n2
    return y


t= multiple(8,9)
print(t)



def divide(r,s):
    l=(r/s)
    return l



l=(90/30)
print("the multiple is",l )
print(l)
print(l)





def mod(o,l): 
    z=o%l
    print("the mod is",z)


o=56
l=79
mod(o,l)



"""def add(a,b):
    return a+b

def subtract(a,b):

a=3
b=4
c=add(3,4)
d=subtract(a,b)
print(d)"""




def add(a,b):
    return a+b

def subtract(x,y):
    return x-y

a= int(input("enter value 1:"))
b= int(input("enter value 2:"))
addResult=add(a,b) #this result will receive the addidtion
    
x=3
y=2   
subtractResult=subtract(addResult,x-y)        
print(subtractResult)



