# import time
# start_time = time.time()


with open("shuffle.in",'r') as f_in:
  n = [int(x) for x in f_in.readline().split(" ")]
  pos = [int(y) for y in f_in.readline().split(" ")]
  l1 = f_in.readline().strip("\n").split(" ")

#l1 = [1234567, 2222222, 3333333, 4444444, 5555555]
#pos = [1,3,4,5,2]

nl1 = []
for j,val in enumerate(pos):
  nl1.insert(j,l1[val-1])

nl2 = []
for j,val in enumerate(pos):
  nl2.insert(j,nl1[val-1])

nl3 = []
for j,val in enumerate(pos):
  nl3.insert(j,nl2[val-1])

with open("shuffle.out","w") as f_out:
    for i in nl3:
        f_out.write(str(i)+"\n")

# following is complicated version... but this works too

# with open("shuffle.in","r") as f_in:
#     N = int(f_in.readline().strip("\n"))
#     shuffle = list(map(int,f_in.readline().strip("\n").split()))
#     ids = f_in.readline().strip("\n").split()
#
# before = {}
# for i in range(1,N+1):
#     before[i] = i
#
# temp = {}
# for i in range(1,N+1):
#     temp[shuffle[i-1]] = before[i]
#
# temp2 = {}
# for i in range(1,N+1):
#     temp2[shuffle[i-1]] = temp[i]
#
# temp3 = {}
# for i in range(1,N+1):
#     temp3[shuffle[i-1]] = temp2[i]
#
# newdict = {}
# for k, v in sorted(temp3.items()):
#     #print(k, v)
#     newdict[v] = ids[k-1]
#
#
# with open("shuffle.out","w") as f_out:
#     for k, v in sorted(newdict.items()):
#         f_out.write(v + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))

