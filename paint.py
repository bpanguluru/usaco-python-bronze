#paint.py

# import time
# start_time = time.time()

with open("paint.in","r") as f_in:
    A, B = map(int,f_in.readline().strip("\n").split())
    C, D = map(int, f_in.readline().strip("\n").split())

overlap = min(B,D) - max(A,C)

result = (B - A) + (D - C)

if overlap > 0:
    result -= overlap

with open("paint.out", "w") as f_out:
    f_out.write(str(result) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
