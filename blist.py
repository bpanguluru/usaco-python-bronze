with open("blist.in", "r") as f_in:
    N = int(f_in.readline().strip("\n"))
    my_list = []
    for _ in range(N):
        s, t, b = map(int, f_in.readline().strip("\n").split())
        my_list.append([s,t,b])

print(my_list)

# with open("blist.out", "w") as f_out:
#         f_out.write(str(m1) +"\n")
#         f_out.write(str(m2) + "\n")
#         f_out.write(str(m3) + "\n")
