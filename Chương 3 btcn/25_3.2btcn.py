m1=int(input('M1='))
m2=int(input('M2='))
m3=int(input('M3='))
t=int(input('S='))
if t<=100:
    print('Phai tra=',m1*t,sep="")
elif t>100 and t<150:
    print('Phai tra=',m2*(t-100)+100*m1,sep="")
elif t>150:
    print('Phai tra=',m3*(t-150)+100*m1+50*m2,sep="")