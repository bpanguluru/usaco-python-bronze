# import time
# start_time = time.time()

with open("mowing.in","r") as f_in:
    N = int(f_in.readline().strip("\n"))
    pattern = []
    for _ in range(N):
        t = f_in.readline().strip("\n").split()
        pattern.append([t[0],int(t[1])])

x = y = t = 0
mydict = {}
min = 9999
for p in pattern:
    # print(p)
    for i in range(p[1]):
        if p[0] == 'N':
            y += 1
        elif p[0] == 'S':
            y -= 1
        elif p[0] == 'W':
            x -= 1
        elif p[0] == 'E':
            x += 1
        t += 1
        # print(x, y, t)
        if (x,y) in mydict:
            if abs(t - mydict[x,y]) < min:
                min =  abs(t - mydict[x,y])
        mydict[x,y] = t

if min == 9999:
    min = -1

with open("mowing.out","w") as f_out:
    f_out.write(str(min)+"\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
