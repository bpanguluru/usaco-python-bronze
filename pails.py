# import time
# start_time = time.time()

with open("pails.in","r") as f_in:
    X, Y, M = map(int,f_in.readline().strip("\n").split())

print(X,Y,M)

x_ctr = 0
result = 0

while x_ctr * X <= M:

    y_ctr = 0

    while x_ctr * X + y_ctr * Y <= M:
        ans = x_ctr * X + y_ctr * Y
        if ans > result:
            result = ans
        y_ctr += 1

    x_ctr += 1

with open("pails.out","w") as f_out:
    f_out.write(str(result)+"\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
