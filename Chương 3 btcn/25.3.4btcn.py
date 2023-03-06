t=float(input(""))
l=float(input(""))
h=float(input(""))
dtb=(t*2+l*3+h)/6
hl=round(dtb,1)
if dtb<3:
    hl='Kem'
elif 3<=dtb<5:
    hl='Yeu'
elif 5<=dtb<6:
    hl='Trung binh'
elif 6<=dtb<7:
    hl='Trung binh kha'
elif 7<=dtb<8:
    hl='Kha'
elif 8<=dtb<9:
    hl='Gioi'
elif 9<=dtb<10:
    hl='Xuat sac'
print(hl)
