# import time
# start_time = time.time()

with open("cowtip.in","r") as f_in:
    N = int(f_in.readline().strip("\n"))
    grid = []
    for _ in range(N):
        grid.append(f_in.readline().strip("\n"))
ctr = 0
while True:
    x = y = -1
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "1":
                x = i
                y = j
    if x == y == -1:
        break
    for i in range(N):
        if i <= x:
            for j in range(N):
                if j <= y:
                    if grid[i][j] == "1":
                        grid[i] = grid[i][:j] + "0" + grid[i][j+1:]
                    else:
                        grid[i] = grid[i][:j] + "1" + grid[i][j+1:]
    ctr += 1

with open("cowtip.out","w") as f_out:
    f_out.write(str(ctr) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
