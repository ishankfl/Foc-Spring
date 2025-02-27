m = 16
n = 3

if n>m:
    temp = n
    n = m
    m = temp
while m%n != 0:
    r= m%n
    m = n
    n = r
    print(m,n)
print(n)
    
    
number = 7
dvd = 1
while number !=0:
    dvd= number * dvd
    number=number-1
print(dvd)