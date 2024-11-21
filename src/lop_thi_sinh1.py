class ThiSinh:
    def __init__(self,name,ngaysinh,diem) -> None:
        self.name = name
        self.ngaysinh = ngaysinh
        self.diem = diem
    def __str__(self) -> str:
        return self.name + ' ' + self.ngaysinh + ' ' + '%.1f'%(self.diem)
name = input()
ngaysinh = input()
t = float(input())
l = float(input())
h = float(input())
print(ThiSinh(name,ngaysinh,(t+l+h)))