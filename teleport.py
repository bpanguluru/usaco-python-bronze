# import time
# start_time = time.time()

with open("teleport.in",'r') as f_in:
  a, b, x, y  = map(int,f_in.readline().strip("\n").split())

option_1 = abs(a-b)
option_2 = abs(a-x) + abs(y-b)
option_3 = abs(a-y) + abs(x-b)

with open("teleport.out","w") as f_out:
    f_out.write(str(min(option_1, option_2, option_3))+"\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))

