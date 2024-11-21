class SinhVien:
    def __init__(self, id, name, team) -> None:
        self.id = id
        self.name = name
        self.team = team
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.team}'
t = int(input())
a = []
while t>0:
    s1 = input()
    s2 = input()
    s = s1 + ' ' + s2
    a.append(s)
    t-=1
q = int(input())
res = []
for i in range(q):
    id = 'C{:03}'.format(i+1)
    name = input()
    tmp = input()
    team = ''
    if tmp=='Team01':
        team = a[0]
    else: team = a[1]
    res.append(SinhVien(id,name,team))
res.sort(key=lambda x : x.name)
for i in res:
    print(i)
# BAV_MIS
# Banking Academy of Vietnam
# FTU Knights1
# Foreign Trade University