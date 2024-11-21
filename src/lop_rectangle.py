class rectangle:
    def __init__(self,dai,rong,mau):
        self.dai = dai
        self.rong = rong
        self.mau = mau.lower().capitalize()
dai,rong,mau = input().split()
if int(dai)<=0 or int(rong)<=0: print('INVALID')
else:
    a = rectangle(int(dai),int(rong),mau)
    print(f'{(a.dai+a.rong)*2} {a.dai*a.rong} {a.mau}')