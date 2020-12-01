# import time
# start_time = time.time()

with open("measurement.in",'r') as f_in:
  N = int(f_in.readline().strip("\n"))
  log = []
  for _ in range(N):
      x = f_in.readline().strip("\n").split()
      log.append([int(x[0]),x[1],x[2]])

log.sort()

dict1 = {"Bessie": 7, "Elsie": 7, "Mildred": 7}

prev_max = 0
prev_winner = ""
result = 0
for x in log:
    if x[2][0] == "+":
        dict1[x[1]] = dict1[x[1]] + int(x[2][1:])
    else:
        dict1[x[1]] = dict1[x[1]] - int(x[2][1:])
    max = 0
    winner = ""
    for k, v in dict1.items():
        if v > max:
            max = v
    for k, v in dict1.items():
        if v == max:
            winner += "," + k

    if winner != prev_winner:
        result += 1
    # print(max,winner)
    prev_max = max
    prev_winner = winner

# print(result)

with open("measurement.out","w") as f_out:
    f_out.write(str(result)+"\n")
# print("time elapsed: {:.2f}s".format(time.time() - start_time))

