#speeding.py

# import time
# start_time = time.time()

with open("speeding.in","r") as f_in:
    N, M = map(int,f_in.readline().strip("\n").split())

    road_speed = []
    for _ in range(N):
        seg, spd = map(int,f_in.readline().strip("\n").split())
        road_speed.append([seg,spd])

    journey_speed = []
    for _ in range(M):
        seg, spd = map(int,f_in.readline().strip("\n").split())
        journey_speed.append([seg,spd])

# print(road_speed[0][1])
dict1 = {}
mile = 0
for i in range(N):
    for j in range(road_speed[i][0]):
        mile += 1
        dict1[mile] = road_speed[i][1]
# print(dict1)

dict2 = {}
mile = 0
for i in range(M):
    for j in range(journey_speed[i][0]):
        mile += 1
        dict2[mile] = journey_speed[i][1]
# print(dict2)

max = 0
for i in range(1,101):
    diff = dict2[i] - dict1[i]
    if diff > 0 and diff > max:
        max = diff

# print(max)


with open("speeding.out", "w") as f_out:
    f_out.write(str(max) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
