n=int(input())
s=len(str(n))
a=n
x=0
while n>0:
    rem=n%10
    n=n//10
    x+=rem**s
print(x)
if a==x:
    print(a,'is armstrong')
else:
    print(a,'is not a armstrong')
    
          
