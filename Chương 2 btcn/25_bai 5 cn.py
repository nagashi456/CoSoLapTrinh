Ten=input('Ho Ten: ')
Cong=float(input('So ngay cong: '))
Don=float(input('Don gia ngay cong: '))
He=float(input('He so phu cap: '))
Tam=float(input('Tam ung: '))
Luong=(Don*Cong*He)
Thuc=(Luong-Tam)
print(f'Nhan vien {Ten}, Co tien luong={Luong}, Tam ung={Tam} va Thuc Linh={Thuc}')