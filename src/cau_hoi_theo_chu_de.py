n = int(input())
ok = 1
d = dict()
tmp = ""
while n>0:
    s = input()
    if len(tmp)==0:
        tmp = s
        d[s] = 0
    elif len(s)==0:
        tmp = ""
    else: d[tmp] +=1
    n-=1
for x in d:
    print(f'{x}: {d[x]}')
# Home/accommodation
# What kind of housing/accommodation do you live in?
# Who do you live with?
# How long have you lived there?

# Study
# Describe your education
# What is your area of specialization?
# Why did you choose to study that major?