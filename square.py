# import time
# start_time = time.time()

with open("square.in","r") as f_in:
    p1_x1, p1_y1, p1_x2, p1_y2 = map(int,f_in.readline().strip("\n").split())
    p2_x1, p2_y1, p2_x2, p2_y2 = map(int,f_in.readline().strip("\n").split())

min_x = min(p1_x1,p1_x2,p2_x1,p2_x2)
max_x = max(p1_x1,p1_x2,p2_x1,p2_x2)
min_y = min(p1_y1,p1_y2,p2_y1,p2_y2)
max_y = max(p1_y1,p1_y2,p2_y1,p2_y2)

x_side = max_x - min_x
y_side = max_y - min_y

result = max(x_side,y_side) ** 2

with open("square.out","w") as f_out:
    f_out.write(str(result)+"\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
