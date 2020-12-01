# import time
# start_time = time.time()

with open("hps.in","r") as f_in:
    N = int(f_in.readline().strip("\n"))
    game = []
    for _ in range(N):
        x = f_in.readline().strip("\n").split()
        game.append([int(x[0]),int(x[1])])

def win(dict1):
    ctr = 0
    for x in game:
        player1 = x[0]
        player2 = x[1]
        if dict1[player1] == "hoof" and dict1[player2] == "scissors":
            ctr += 1
        elif dict1[player1] == "scissors" and dict1[player2] == "paper":
            ctr += 1
        elif dict1[player1] == "paper" and dict1[player2] == "hoof":
            ctr += 1
    return ctr

max = 0
dict1 = {1:"hoof", 2:"paper", 3:"scissors"}
t = win(dict1)
if t > max:
    max = t
dict1 = {1:"hoof", 2:"scissors", 3:"paper"}
t = win(dict1)
if t > max:
    max = t
dict1 = {1:"paper", 2:"hoof", 3:"scissors"}
t = win(dict1)
if t > max:
    max = t
dict1 = {1:"paper", 2:"scissors", 3:"hoof"}
t = win(dict1)
if t > max:
    max = t
dict1 = {1:"scissors", 2:"hoof", 3:"paper"}
t = win(dict1)
if t > max:
    max = t
dict1 = {1:"scissors", 2:"paper", 3:"hoof"}
t = win(dict1)
if t > max:
    max = t

# print(max)

with open("hps.out","w") as f_out:
    f_out.write(str(max) + "\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
