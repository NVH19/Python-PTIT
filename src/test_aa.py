# src = open('\Python_codeptit\Python_codeptit\DATA.in','r')
# s = src.read().split('\n')
# def tong(s):
#     sum = 0
#     for i in s:
#         sum += int(i)
#     return sum
# for i in s:
#     res = 0
#     tmp = ''
#     a = []
#     for j in i:
#         if j.isdigit():
#             res = res*10 + int(j)
#         else:
#             if res>0:
#                 tmp+=str(res)
#             res = 0
#     if res>0: tmp+=str(res)
#     print(tmp + ' ' + str(tong(tmp)))

# from collections import Counter
# a = [5,2,3,4,2,1,3,4,5,2,5]
# s = Counter(a)
# for i in s:
#     print(f'{i} {s[i]}')

a = '2021/2022'
a = a.replace('/',' ')
print(a)