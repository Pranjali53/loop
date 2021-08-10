num=int(input("enter the name:-"))
count=0
i=1
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print(num,"is prime number")
else:
    print(num,"is not prime number")


num=int(input("enter the name:-"))
count=0
i=2
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==1:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")



num=int(input("enter the name:-"))
i=2
while i<num:
    if num%i==0:
       print(num,"is not a prime number")
       break
    i+=1
else:
    print(num,"is a prime number") 


