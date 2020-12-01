# import time
# start_time = time.time()

with open("learning.in","r") as f_in:
    n, a, b = [int(x) for x in f_in.readline().split()]
    cows = []
    for _ in range(n):
        x = f_in.readline().split()
        cows.append([x[0],int(x[1])])
    cows.append(["NS",-1000000000])
    cows.append(["NS",1000000000])
    cows_sorted = sorted(cows, key = lambda cow: cow[1])

ctr = 0

for i in range(len(cows_sorted)-1):

    S = cows_sorted[i][1]
    E = cows_sorted[i+1][1]
    M = (S + E) // 2

    if cows_sorted[i][0] == 'S':
        s = max(a, S+1)
        e = min(b, M)
        if e >= s:
            ctr += e - s + 1

    if cows_sorted[i+1][0] == 'S':
        s = max(a, M+1)
        e = min(b, E)
        if e >= s:
            ctr += e - s + 1

    if cows_sorted[i][0] == 'NS' and cows_sorted[i+1][0] == 'S' and S % 2 == E % 2 and a <= M <= b:
        ctr += 1

with open("learning.out", "w") as f_out:
    f_out.write(str(ctr) + "\n")



# print("time elapsed: {:.2f}s".format(time.time() - start_time))
