print("Calculator")
print("1 - Sum")
print("2 - Sub")
print("3 - Multi")
print("4 - Div")
ch=int(input("Enter ur choise : "))
a=int(input("Enter the first no"))
b=int(input("Enter the first no"))

if(ch==1):
    c=a+b
elif(ch==2):
    c=a-b
elif(ch==3):
    c=a*b
elif(ch==4):
    c=a//b
else:
    print("Invalid Choice")
    c=0

print("Result = ", c)