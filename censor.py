#censor.py

# import time
# start_time = time.time()

with open("censor.in","r") as f_in:
    S = f_in.readline().strip("\n")
    T = f_in.readline().strip("\n")

new_S = ""
len_T = len(T)

for x in S:
    new_S += x
    st = len(new_S) - len_T
    if new_S[st:] == T:
        new_S = new_S[:st]


with open("censor.out", "w") as f_out:
    f_out.write(new_S + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
