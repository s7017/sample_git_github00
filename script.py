z=input()
a=0
b=0
c=0
d=0
sum=0
for i in z:
    if i== ">":
        a+=1
        b=0
        c-=1
        if c==-1:
            c=0
        d+=1
    else:
        if d!=0:
            for n in range(a,0,-1):
                sum+=n
                a-=1
        b+=1
        c+=1
        d=0
        print(sum)
if b!=0:
    for n in range(b,0,-1):
        sum+=n
if c!=0 and b-c!=0:
    for n in range(a,0,-1):
        sum+=c
        c-=1
if d!=0 and c==0:
    for n in range(d,0,-1):
        sum+=n



print(sum)
