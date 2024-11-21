class SinhVien:
    def __init__(self, msv, name, lop, diem) -> None:
        self.msv = msv
        self.name = name
        self.lop = lop
        self.diem = diem
    def __str__(self) -> str:
        if self.diem<=0:
            self.diem = '0 KDDK'
        return self.msv + ' ' + self.name + ' ' + self.lop + ' ' + str(self.diem)
t = int(input())
a = {}
for i in range(t):
    msv = input()
    name = input()
    lop = input()
    diem = 10
    a[msv] = SinhVien(msv,name,lop,diem)
while t>0:
    t-=1
    s = input().split()
    id = s[0]
    cc = s[1]
    for i in cc:
        if i=='v':
            a[id].diem -= 2
        elif i=='m':
            a[id].diem -= 1
for i in a:
    print(a[i])
# B19DCCN999
# Le Cong Minh
# D19CQAT02-B
# B19DCCN998
# Tran Truong Giang
# D19CQAT02-B
# B19DCCN997
# Nguyen Tuan Anh
# D19CQCN04-B
# B19DCCN998 xxxmxmmvmx
# B19DCCN997 xmxmxxxvxx
# B19DCCN999 xvxmxmmvvm