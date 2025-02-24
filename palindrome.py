num=int(input("Enter a number= "))
sum=0
temp=num 
l=len(str(num))
print(l)
while temp>0:
    digit=temp%10
    sum=sum+(digit*(10**(l-1)))
    temp=temp//10
    l-=1
if(num==sum):
        print(num,"is a palindrome number")
else:
        print(num,"is not a palindrome number")