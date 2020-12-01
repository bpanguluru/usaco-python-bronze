
with open("angry.in","r") as f_in:
    N = int(f_in.readline().strip("\n"))
    positions = [int(x) for x in f_in.read().strip("\n").split("\n")]

def blast(source,distance):
    global done

    target = []
    for s in source:
        for t in positions:
            if t in done:
                continue
            if abs(s-t) <= distance:
                target.append(t)
                done.append(t)

    if len(target) == 0:
        return
    else:
        blast(target,distance+1)

max_blast = 0
for x in positions:
    done = [x]
    source = [x]
    distance = 1
    blast(source,distance)
    if len(done) > max_blast:
        max_blast = len(done)

with open("angry.out","w") as f_out:
    f_out.write(str(max_blast)+"\n")
