#hopscotch.py

# import time
# start_time = time.time()

with open("hopscotch.in","r") as f_in:
    R, C = map(int,f_in.readline().strip("\n").split())
    hs = f_in.read().strip("\n").split("\n")

result = 0
def dfs(r_pos,c_pos):
    global result

    if r_pos == R - 1 and c_pos == C - 1:
        result += 1
        return

    for x in range(r_pos+1,R):
        for y in range(c_pos+1,C):
            if hs[x][y] != hs[r_pos][c_pos]:
                dfs(x,y)

dfs(0,0)

with open("hopscotch.out", "w") as f_out:
    f_out.write(str(result) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
