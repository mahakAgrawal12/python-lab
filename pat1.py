l1=[1,3,4,2]
l2=[1,4,9,5]
l4=l1+l2
[l4.remove(x) for x in l4 if x in l1 and x in l2]
print(l4)
