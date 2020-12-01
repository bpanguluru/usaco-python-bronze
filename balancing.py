# import time
# start_time = time.time()

with open("balancing.in","r") as f_in:
    N, B = map(int,f_in.readline().strip("\n").split())
    locations = []
    for _ in range(N):
        x, y = map(int,f_in.readline().strip("\n").split())
        locations.append([x,y])

x_set = set()
y_set = set()

for l in locations:
    x_set.add(l[0])
    y_set.add(l[1])

min_bal = 100

for x in x_set:
    for y in y_set:
        a = x + 1
        b = y +1
        first = second = third = fourth = 0
        for l in locations:
            if l[0] > a and l[1] > b:
                first += 1
            elif l[0] < a and l[1] > b:
                second += 1
            elif l[0] < a and l[1] < b:
                third += 1
            elif l[0] > a and l[1] < b:
                fourth += 1
        max_count = max(first,second,third,fourth)
        if max_count < min_bal:
            min_bal = max_count

with open("balancing.out","w") as f_out:
    f_out.write(str(min_bal)+"\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
