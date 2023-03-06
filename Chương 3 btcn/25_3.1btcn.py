import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
p=float((a+b+c)/2)
s=float(math.sqrt(p*(p-a)*(p-b)*(p-c)))
if (a+b)>c and (a+c)>b and (b+c)>a:
    print('Dien tich='+str(round(s,3)))
else:
    print('Khong hop le')            
            