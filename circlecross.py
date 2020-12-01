# import time
# start_time = time.time()

with open("circlecross.in","r") as f_in:
    ALPHA_TWICE = f_in.readline().strip("\n")

i = ctr = 0
new_alpha = ""
while True:
    if ALPHA_TWICE[i] == ALPHA_TWICE[i+1]:
        ctr += 2
        i += 2
    else:
        new_alpha += ALPHA_TWICE[i]
        i += 1
    if i > 50:
        break

pairs = []
for i, v in enumerate(new_alpha):
    for j in range(i+1,len(new_alpha)):
        if v == new_alpha[j]:
            continue
        pair = [v,new_alpha[j]]
        if pair not in pairs:
            pairs.append(pair)
        else:
            pairs.remove(pair)

with open("circlecross.out","w") as f_out:
    f_out.write(str(len(pairs)//2) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))

