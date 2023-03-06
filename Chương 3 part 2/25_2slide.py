s=0
n=int(input('n='))
for i in range(1,n+1):
    if n%i==0:
        s=s+1
if s==2:
    print(n,"la SNT")
else:
    print(n,"khong la SNT")
# n=int(input('n='))
# i=2
# for i in range(2,n-1):
#     if n%i==0 :
#         print(n,'khong la SNT')
#     else:
#         print(n,'la SNT')