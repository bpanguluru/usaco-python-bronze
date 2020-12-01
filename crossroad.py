# import time
# start_time = time.time()

with open("crossroad.in","r") as f_in:
    N = int(f_in.readline().strip("\n"))
    observations = []
    for _ in range(N):
        x = f_in.readline().strip("\n").split()
        observations.append([int(x[0]),int(x[1])])
dict1 = {1:-1,2:-1,3:-1,4:-1,5:-1,6:-1,7:-1,8:-1,9:-1,10:-1}

ctr = 0
for o in observations:
    if dict1[o[0]] == -1:
        dict1[o[0]] = o[1]
    else:
        if o[1] != dict1[o[0]]:
            ctr += 1
            dict1[o[0]] = o[1]

with open("crossroad.out","w") as f_out:
    f_out.write(str(ctr) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
