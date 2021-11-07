import os, random
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
g = []
path = 
os.mkdir(path=path)
while len(g) != 5:
    b = random.choices(a)
    if b not in g:
        g.append(b)
        file = open(f'{path}\\{b}.py', 'w')
    print(g)