with open("badmilk.in","r") as f_in:
    N, M, D, S = map(int,f_in.readline().strip("\n").split())

    drink = []
    for _ in range(D):
        p, m, t = map(int,f_in.readline().strip("\n").split())
        drink.append([p,m,t])

    sick = []
    for _ in range(S):
        p, t = map(int,f_in.readline().strip("\n").split())
        sick.append([p,t])

dict1 = {}
for x in sick:
    p1 = x[0]
    t1 = x[1]

    for y in drink:
        p2 = y[0]
        m2 = y[1]
        t2 = y[2]
        if p1 != p2:
            continue
        if t2 >= t1:
            continue
        if p1 not in dict1:
            dict1[p1] = [m2]
        else:
            t = dict1[p1]
            t.append(m2)
            dict1[p1] = t

bad_milk = set() #set
first = True
for i, v in dict1.items():
    if first:
        bad_milk = set(v)
        first = False
    else:
        bad_milk = bad_milk & set(v)
    print(set(v), bad_milk)

max = 0
for x in bad_milk:
    ppl = set()
    for y in drink:
        if y[1] == x:
            ppl.add(y[0])
    if len(ppl) > max:
        max = len(ppl)

with open("badmilk.out", "w") as f_out:
    f_out.write(str(max) + "\n")

