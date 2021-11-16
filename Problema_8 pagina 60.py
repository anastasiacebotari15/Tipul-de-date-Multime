a={1,2,3}
b={3,4,5}
print('a) Intersectia multimilor A si B:',a.intersection(b))
print('b) Reuniunea multimilor A si B:',a.union(b))
print('c) Diferenta multimilor A si B:',a.difference(b))



a=set(input('Elementele multimii A:'))
b=set(input('Elementele multimii B:'))
if type(a) is int:
    if type(b) is int:
        print('a) Intersectia multimilor A si B:',a.intersection(b))
        print('b) Reuniunea multimilor A si B:',a.union(b))
        print('c) Diferenta multimilor A si B:',a.difference(b))