n = input("Enter n: ")
m = input("Enter m: ")
while (m<=n):
    print "enter again..."
    n = input("Enter n: ")
    m = input("Enter m: ")
sum=0
for i in range(n,m):
    z=i+1
    if(z%n==0):
        sum=sum+z
print sum
