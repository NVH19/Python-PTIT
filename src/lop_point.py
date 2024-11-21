import math
class Point:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def distance(self,p2):
        x = self.a-p2.a
        y = self.b-p2.b
        res = math.sqrt(x*x+y*y)
        return "{:.4f}".format(res)
def Decimal(s):
    return float(s)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1