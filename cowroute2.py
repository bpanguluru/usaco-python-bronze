# import time
# start_time = time.time()

with open("cowroute2.in","r") as f_in:
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
    if A not in r:
        continue

    index_A = r.index(A)
    for i, u in enumerate(r):
        if i < index_A:
            u2b[u] = prices[ir][0]
        elif i > index_A:
            a2u[u] = prices[ir][0]

result = 9999

for i in range(250000):
    if i in a2u and i in u2b:
        result = min(a2u[i]+u2b[i], result)


if result == 9999:
    result = -1

with open("cowroute2.out", "w") as f_out:
    f_out.write(str(result) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
