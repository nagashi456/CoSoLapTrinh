# i=1
# while i<18 and i>=1:
#     j=17
#     while i-1<=j:
#         print(" ",end="")
#         j=j-2
#     k=1
#     while k<=i:
#         print('*',end="")

#         k=k+1
#     print("")
#     i=i+2
i=1
while i<18 and i>=1:
    n=17
    print(' '*((n-i)//2),end='')
    print('*'*i)
    i=i+2