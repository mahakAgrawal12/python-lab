t=[]
for i in range(2000,3300):
        if((i%7==0)&(i%5!=0)):
                t.append(i)
                m=tuple(t)
                print(m)
