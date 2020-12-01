with open("marathon.in","r") as f_in:
    N = int(f_in.readline().strip("\n"))
    check_points = []
    for _ in range(N):
        check_points.append(list(map(int,f_in.readline().split())))

totalDistance = 0
for i in range(1,N):
    totalDistance += abs(check_points[i][0] - check_points[i-1][0]) + abs(check_points[i][1] - check_points[i-1][1])

largestSkip = 0
for i in range(1,N-1):
    noSkipDistance = abs(check_points[i][0] - check_points[i-1][0]) + abs(check_points[i+1][0] - check_points[i][0]) + abs(check_points[i][1] - check_points[i-1][1]) + abs(check_points[i+1][1] - check_points[i][1])
    skipDistance = abs(check_points[i+1][0] - check_points[i-1][0]) + abs(check_points[i+1][1] - check_points[i-1][1])
    largestSkip = max(largestSkip, noSkipDistance  - skipDistance)

with open("marathon.out","w") as f_out:
    f_out.write(str(totalDistance - largestSkip)+"\n")