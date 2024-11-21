# t = int(input())
# a = {}
# for i in range(t):
#     date = input()
#     time = input()
#     phong = input()
#     # res = "C" 
#     a[i] = [date, time, phong]

# b=dict(sorted(a.items(), key=lambda x:(x[1])))
# for i in b:
#     print(i, b[i][0], b[i][1], b[i][2])

class Ds():
    def __init__(self, id, date, time, phong):
        self.id=id
        self.date=date
        self.time=time
        self.phong=phong
    def show(self):
        return f'{self.id} {self.date} {self.time} {self.phong}'
if __name__=='__main__':
    t = int(input())
    a = []
    for i in range(t):
        date = input()
        time = input()
        phong = input()
        a.append(Ds(("C"+str(i+1).zfill(3)),date, time, phong))
    a.sort(key=lambda x:(x.time))
for i in a:
    print (i.show())

# 2
# 09/01/2022
# 15:30
# 70172
# 09/01/2022
# 10:00
# 70279