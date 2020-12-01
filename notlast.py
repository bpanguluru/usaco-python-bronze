# import time
# start_time = time.time()

with open("notlast.in","r") as f_in:
    N = int(f_in.readline().strip("\n"))
    entries = []
    for _ in range(N):
        x = f_in.readline().strip("\n").split()
        entries.append([x[0],int(x[1])])
mydict = {"Bessie": 0, "Elsie": 0, "Daisy":0, "Gertie": 0, "Annabelle": 0, "Maggie": 0, "Henrietta": 0}

for e in entries:
    mydict[e[0]] = mydict[e[0]] + e[1]
# print(mydict)
min = 999999
for k, v in mydict.items():
    if v < min:
        min = v
# print(min)
next_min = 999999
name = "Tie"
for k, v in mydict.items():
    if v == min:
        continue
    if v < next_min:
        next_min = v
        name = k
# print(next_min,name)
if name != "Tie":
    ctr = 0
    for k, v in mydict.items():
        if v == next_min:
            ctr += 1
    if ctr > 1:
        name = "Tie"

with open("notlast.out","w") as f_out:
    f_out.write(name + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
