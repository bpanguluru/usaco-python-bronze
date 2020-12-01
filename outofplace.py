# import time
# start_time = time.time()

with open("outofplace.in",'r') as f_in:
  N  = int(f_in.readline().strip("\n"))
  hights = []
  for _ in range(N):
      hights.append(int(f_in.readline().strip("\n")))

ctr = -1
for h, hs in zip(hights, sorted(hights)):
    if h != hs:
        ctr += 1

with open("outofplace.out","w") as f_out:
    f_out.write(str(max(ctr,0))+"\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))

