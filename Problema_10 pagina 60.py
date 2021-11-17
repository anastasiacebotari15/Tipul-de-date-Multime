import itertools
a = {1,2,3,4}
c = itertools.combinations(a,0)
d=itertools.combinations(a,1)
e=itertools.combinations(a,2)
f=itertools.combinations(a,3)
b = set(c)
b1=set(d)
b2=set(e)
b3=set(f)
print('Submultimile multimii A sunt:',b,b1,b2,b3)