# import time
# start_time = time.time()

with open("cowqueue.in","r") as f_in:
    N = int(f_in.readline().strip("\n"))
    time_log = []
    for _ in range(N):
        x = f_in.readline().strip("\n").split()
        time_log.append([int(x[0]), int(x[1])])
time_log.sort()

for i, x in enumerate(time_log):
    arr_time = x[0]
    req_time = x[1]
    if i == 0:
        end_time = arr_time + req_time
        continue
    if arr_time < end_time:
        end_time = end_time + req_time
    else:
        end_time = arr_time + req_time


with open("cowqueue.out","w") as f_out:
    f_out.write(str(end_time) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))

