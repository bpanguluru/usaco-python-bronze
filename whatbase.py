# import time
# start_time = time.time()

with open("whatbase.in","r") as f_in:
    K = int(f_in.readline())
    base = []
    for _ in range(K):
        x = f_in.readline().split()
        base.append([x[0],x[1]])

def evaluate(inum,ibase):
    return( int(inum[0]) * ibase * ibase + int(inum[1]) * ibase + int(inum[2]))

result = []

for i in range(K):

    num1 = base[i][0]
    num2 = base[i][1]

    X = 10
    Y = 10

    while X <= 15000 and Y <= 15000:
        N_X = evaluate(num1,X)
        N_Y = evaluate(num2,Y)
        if N_X < N_Y:
            X += 1
        elif N_X > N_Y:
            Y += 1
        else:
            result.append([X, Y])
            break

with open("whatbase.out", "w") as f_out:
    for i in range(K):
        f_out.write(str(result[i][0]) + " " + str(result[i][1]) + "\n")







# print("time elapsed: {:.2f}s".format(time.time() - start_time))