# import time
# start_time = time.time()

with open("meeting.in","r") as f_in:
    N, M = [int(x) for x in f_in.readline().split()]
    paths = []
    for _ in range(M):
        x = f_in.readline().split()
        paths.append([int(x[0]),int(x[1]),int(x[2]),int(x[3])])

bcan = {}
ecan = {}

def test2(st,tm_b,tm_e):
    if st == N:
        bcan[tm_b] = True
        ecan[tm_e] = True
        return

    for x in paths:
        if x[0] == st:
            test2(x[1],tm_b+x[2],tm_e + x[3])

test2(1,0,0)

max_time = max(max(bcan), max(ecan))

ans = -1
for x in range(1,max_time):
    if x in bcan and x in ecan:
        ans = x
        break

with open("meeting.out", "w") as f_out:
    if ans == -1:
        f_out.write("IMPOSSIBLE" + "\n")
    else:
        f_out.write(str(x) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
