# import time
# start_time = time.time()
from string import ascii_lowercase

with open("blocks.in","r") as f_in:
    N = int(f_in.readline().strip("\n"))
    words = []
    for _ in range(N):
        word1, word2 = f_in.readline().strip("\n").split()
        words.append([word1,word2])

# #getting combinations
# def dfs(pos,comb):
#     comb2 = comb.copy()
#     for i, x in enumerate(words[pos]):
#         if i == 1:
#             comb2 = comb.copy()
#         comb2.append(x)
#         #print(comb2)
#         if pos+1 != len(words):
#             dfs(pos+1,comb2)
#         else:
#             print(comb2)
# comb2 = []
# dfs(0,comb2)


letters = []
for ws in words:
    word1 = list(ws[0])
    word2 = list(ws[1])

    for x in word1:
        letters.append(x)
        if x in word2:
            word2.remove(x)
    for x in word2:
        letters.append(x)
counts = []
for l in ascii_lowercase:
    counts.append(letters.count(l))

with open("blocks.out","w") as f_out:
    for count in counts:
        f_out.write(str(count)+"\n")

# print("time elapsed: {:.2f}s".format(time.time() - start_time))
