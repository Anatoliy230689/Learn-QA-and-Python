with open ('new.txt','r') as f:
    new = f.read()

sort = sorted(new.split())
res =[]

for i in range(len(sort)):
    if (sort[i] != sort[i-1]):
        res.append(f'{sort[i]} , {sort.count(sort[i])}')

with open("output.txt", "w") as file:
    print(*res, sep='\n', file=file)





