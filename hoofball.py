# import time
# start_time = time.time()

with open("hoofball.in",'r') as f_in:
  N  = int(f_in.readline().strip("\n"))
  hb = [int(x) for x in f_in.readline().strip("\n").split()]

hb.sort()

def target(i):
    prev_dist = -1
    next_dist = -1

    if i > 0:
         prev_dist = hb[i] - hb[i-1]

    if i < N - 1:
        next_dist = hb[i+1] - hb[i]

    if prev_dist == -1:
        return(i+1)
    elif next_dist == -1:
        return(i-1)
    elif prev_dist > next_dist:
        return(i+1)
    else:
        return(i-1)

passto = {}
for i in range(N):
    passto[i] = 0

for i in range(N):
    passto[target(i)] += 1

ctr = 0
for i in range(N):
    if passto[i] == 0:
        ctr += 1
    if (i < target(i) and target(target(i)) == i and passto[i] == 1 and passto[target(i)] == 1):
        ctr += 1

with open("hoofball.out","w") as f_out:
    f_out.write(str(ctr)+"\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))

