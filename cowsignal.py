# import time
# start_time = time.time()

with open("cowsignal.in","r") as f_in:
    M, N, K = map(int,f_in.readline().strip("\n").split())
    signals = []
    for _ in range(M):
        signals.append(f_in.readline().strip("\n"))

new_signals = []
for signal in signals:
    new_signal = ""
    for s in signal:
        new_signal += s * K
    for i in range(K):
        new_signals.append(new_signal)




with open("cowsignal.out","w") as f_out:
    for nw in new_signals:
        f_out.write(nw + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
