# import time
# start_time = time.time()

with open("cbarn.in","r") as f_in:
    n = int(f_in.readline().strip("\n"))
    r = []
    for _ in range(n):
        r.append(int(f_in.readline().strip("\n")))

ans = n * n *100
for i in range(n):

    tot = 0

    for i, v in enumerate(r):
        tot += i * v

    if tot < ans:
        ans = tot

    t = r.pop(0)
    r.append(t)

with open("cbarn.out","w") as f_out:
    f_out.write(str(ans)+"\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
