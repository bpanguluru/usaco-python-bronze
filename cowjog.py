with open("cowjog.in","r") as f_in:
    N = int(f_in.readline())
    jog = []
    for _ in range(N):
        x = f_in.readline().split()
        jog.append([int(x[0]),int(x[1])])

ctr = 0
for i in range(N-1,0,-1):
    if jog[i][1] < jog[i-1][1]:
        jog[i - 1][1] = jog[i][1]
        ctr += 1

with open("cowjog.out","w") as f_out:
    f_out.write(str(N-ctr) + "\n")