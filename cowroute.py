#cowroute_two.py

# import time
# start_time = time.time()

with open("cowroute.in","r") as f_in:
    A, B, N = [int(x) for x in f_in.readline().split()]
    routes = []
    prices = []
    for _ in range(N):
        x = f_in.readline().split()
        prices.append([int(x[0]),int(x[1])])
        x = f_in.readline().split()
        route = []
        for i in x:
            route.append(int(i))
        routes.append(route)

a2u = {}
u2b = {}

for ir, r in enumerate(routes):

    if A in r:
        index_A = r.index(A)
    else:
        index_A = len(r)

    if B in r:
        index_B = r.index(B)
    else:
        index_B = -1

    for i, u in enumerate(r):
        if i <= index_B:
            if u in u2b:
                u2b[u] = min(u2b[u],prices[ir][0])
            else:
                u2b[u] = prices[ir][0]
        if i >= index_A:
            if u in a2u:
                a2u[u] = min(a2u[u],prices[ir][0])
            else:
                a2u[u] = prices[ir][0]

result = 9999

for i in range(250000):
    res = 0
    if i in a2u and i in u2b:
        if i != A:
            res = a2u[i]
        if i != B:
            res += u2b[i]
        result = min(res, result)

if result == 9999:
    result = -1

with open("cowroute.out", "w") as f_out:
    f_out.write(str(result) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
