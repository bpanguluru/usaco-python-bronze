# import time
# start_time = time.time()

with open("lifeguards.in",'r') as f_in:
  N  = int(f_in.readline().strip("\n"))
  shifts = []
  for _ in range(N):
      x = f_in.readline().strip("\n").split()
      shifts.append([int(x[0]),int(x[1])])

shifts.sort()

numcover = {}
for t in range(1000):
    numcover[t] = 0

for s in shifts:
    for t in range(s[0],s[1]):
        numcover[t] += 1

max = 0
for s in shifts:
    for t in range(s[0],s[1]):
        numcover[t] -= 1

    cover_count = 0
    for t in range(1000):
        if numcover[t] > 0:
            cover_count += 1

    for t in range(s[0],s[1]):
        numcover[t] += 1

    if cover_count > max:
        max = cover_count

with open("lifeguards.out","w") as f_out:
    f_out.write(str(max)+"\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))

