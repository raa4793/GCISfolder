"""print("2"+"4")
print (int("23"))



print (float("2"+"4"))
#for boolean expression true=1,false=0
a=False
print(int(a))
print(float(10))"""
def information(name,age,degree_program,is_active):
    info= name,age,degree_program,is_active
    return info

def main():
    names=input("enter the name:")
    ages=input(int("enter the age:"))
    deg=input("enter the program:")
    isactive=bool(input("Are you active?1 for yes;0 for no"))
    print(information(names,ages,deg,isactive))


main()
