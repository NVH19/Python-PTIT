class SV:
    def __init__(self,name,point,sub):
        self.name = name
        self.point = point
        self.sub = sub
a = []
t = int(input())
while t>0:
    name = input()
    point,sub = map(int,input().split())
    a.append(SV(name,point,sub))
    t-=1
a = sorted(a,key=lambda x:(x.name))
a = sorted(a,key=lambda x:(x.sub))
a = sorted(a,key=lambda x:(x.point), reverse=True)
for i in a:
    print(f'{i.name} {i.point} {i.sub}')