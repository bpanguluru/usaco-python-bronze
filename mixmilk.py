with open("mixmilk.in", "r") as f_in:
    c1, m1 = list(map(int,f_in.readline().strip("\n").split()))
    c2, m2 = list(map(int, f_in.readline().strip("\n").split()))
    c3, m3 = list(map(int, f_in.readline().strip("\n").split()))

def pour(ca, ma, cb, mb):
    pour_amt = min(ma, cb - mb)
    ma -= pour_amt
    mb += pour_amt
    return ma, mb

for i in range(33):
    m1, m2 = pour(c1, m1, c2, m2)
    m2, m3 = pour(c2, m2, c3, m3)
    m3, m1 = pour(c3, m3, c1, m1)

m1, m2 = pour(c1, m1, c2, m2)

with open("mixmilk.out", "w") as f_out:
        f_out.write(str(m1) +"\n")
        f_out.write(str(m2) + "\n")
        f_out.write(str(m3) + "\n")
