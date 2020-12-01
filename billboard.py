# import time
# start_time = time.time()

with open("billboard.in",'r') as f_in:
  lm_x1, lm_y1, lm_x2, lm_y2  = map(int,f_in.readline().strip("\n").split())
  cf_x1, cf_y1, cf_x2, cf_y2  = map(int,f_in.readline().strip("\n").split())

lm_width = lm_x2 - lm_x1
lm_hight = lm_y2 - lm_y1

overlap_x1 = max(lm_x1, cf_x1)
overlap_y1 = max(lm_y1, cf_y1)
overlap_x2 = min(lm_x2, cf_x2)
overlap_y2 = min(lm_y2, cf_y2)

result = lm_width * lm_hight

if overlap_x2 > overlap_x1 and overlap_y2 > overlap_y1:
    overlap_width = overlap_x2 - overlap_x1
    overlap_hight = overlap_y2 - overlap_y1
    if overlap_width == lm_width:
        if overlap_y1 > lm_y1 and overlap_y2 < lm_y2:
            pass
        else:
            result = lm_width * (lm_hight - overlap_hight)
    elif overlap_hight == lm_hight:
        if overlap_x1 > lm_x1 and overlap_x2 < lm_x2:
            pass
        else:
            result = lm_hight * (lm_width - overlap_width)

with open("billboard.out","w") as f_out:
    f_out.write(str(result)+"\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))

