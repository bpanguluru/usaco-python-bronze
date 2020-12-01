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

result = 9999
for i in range(N):
    route = routes[i]
    #print(route)
    if A in route and B in route and route.index(A) < route.index(B):
        result = min(result,prices[i][0])

if result == 9999:
    result = -1

with open("cowroute.out", "w") as f_out:
    f_out.write(str(result) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
