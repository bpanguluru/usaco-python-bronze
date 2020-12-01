# import time
# start_time = time.time()

with open("billboard.in","r") as f_in:
    b1_x1, b1_y1, b1_x2, b1_y2 = map(int,f_in.readline().strip("\n").split())
    b2_x1, b2_y1, b2_x2, b2_y2 = map(int,f_in.readline().strip("\n").split())
    t_x1, t_y1, t_x2, t_y2 = map(int,f_in.readline().strip("\n").split())

b1_area = abs(b1_x1 - b1_x2) * abs(b1_y1 - b1_y2)
b2_area = abs(b2_x1 - b2_x2) * abs(b2_y1 - b2_y2)

o1_x1 = max(b1_x1, t_x1)
o1_y1 = max(b1_y1, t_y1)
o1_x2 = min(b1_x2, t_x2)
o1_y2 = min(b1_y2, t_y2)

if o1_x2-o1_x1 > 0 and o1_y2-o1_y1 > 0:
    b1_area -= (o1_x2-o1_x1) * (o1_y2-o1_y1)

o2_x1 = max(b2_x1, t_x1)
o2_y1 = max(b2_y1, t_y1)
o2_x2 = min(b2_x2, t_x2)
o2_y2 = min(b2_y2, t_y2)
if o2_x2 - o2_x1 > 0 and o2_y2 - o2_y1 > 0:
    b2_area -= (o2_x2 - o2_x1) * (o2_y2 - o2_y1)

result = b1_area + b2_area

with open("billboard.out","w") as f_out:
    f_out.write(str(result) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))

