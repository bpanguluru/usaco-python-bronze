with open("taming.in", "r") as f_in:
    n1 = int(f_in.readline())
    log = [int(x) for x in f_in.readline().split(" ")]
# print(log)
r_log = reversed(log)
st = 0
new_rlog = []

for i, v in enumerate(r_log):
    # print(i,v)

    if v >= 0:
        st = v
        new_rlog.append(v)

    if v == -1:
        if i == len(log) - 1:
            new_rlog.append(0)
        elif st > 0:
            st -= 1
            new_rlog.append(st)
        else:
            new_rlog.append(v)
    # print(new_rlog)

ans = list(reversed(new_rlog))
# print(ans)
bad = False
for i, v in enumerate(ans):
    if i == len(ans) - 1:
        continue
    n = ans[i + 1]
    if v >= 0:
        if n == 0 or n == -1 or n == v + 1:
            pass
        else:
            # print("hello",i,v)
            bad = True

with open("taming.out", "w") as f_out:
    if bad == True:
        # print(-1)
        f_out.write(str(-1))
    else:
        # print(ans.count(0), ans.count(0) + ans.count(-1))
        f_out.write(str(ans.count(0)) + " " + str(ans.count(0) + ans.count(-1)))


