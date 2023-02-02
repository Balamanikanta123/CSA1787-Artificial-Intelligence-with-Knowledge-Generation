a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
print("1.addition 2.subtraction 3.multiplication 4.division")
ch=int(input("enter your choice:"))
if(ch==1):
    n1=(a+b)
    print(n1)
elif(ch==2):
    n2=(a-b)
    print(n2)
elif(ch==3):
    n3=(a*b)
    print(n3)
elif(ch==4):
    n4=(a/b)
    print(n4)
else:
    print("choose the correcrt choice")

