#cow.py

# import time
# start_time = time.time()

with open("cow.in","r") as f_in:
    N = f_in.readline().strip("\n")
    cow_str = f_in.readline().strip("\n")

c = co = cow = 0

for x in cow_str:
    if x == 'C':
        c += 1
    elif x == 'O':
        co += c
    elif x == 'W':
        cow += co

with open("cow.out", "w") as f_out:
    f_out.write(str(cow) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
