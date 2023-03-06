# i=1 
# while i<=6:
#     j=1
#     k=6
#     while k<=i:
#         print(" "*(k-i),end="")
#         k=k-1
#     print('')
#     while j<=i:
#         print("*"*i)
#         j=j+1
#     i=i+1
# i=1
# n=6
# while i<=n:
#     print(" "*(n-i),end="")
#     print("*"*i)
#     i=i+1
d=str(input())
n=int(input())
i=1
while 1<=n<=20 and i<=n:
    j=1
    while j<=i:
        print(d,end=" ")
        j=j+1
    print('')
    i=i+1
print('Khong hop le')