with open("crosswords.in","r") as f_in:
    n, m = map(int,f_in.readline().split())
    crossword = f_in.read().strip("\n").split("\n")

print(n,m)
print(crossword)

clues = []
clue_count = 0
for x in range(n):
    for y in range(m):
        if crossword[x][y] == '#':
            continue

        clue = False

        # horizontal clue
        if (y == 0 or (y > 0 and crossword[x][y-1] == "#")) and (y < m - 2 and crossword[x][y + 1] == "." and crossword[x][y + 2] == "."):
            clue = True

        # vertical clue
        if (x == 0 or (x > 0 and crossword[x-1][y] == "#")) and (x < n - 2 and crossword[x+1][y] == "." and crossword[x+2][y] == "."):
            clue = True

        if clue:
            clues.append([x + 1, y + 1])
            clue_count += 1

with open("crosswords.out","w") as f_out:
    f_out.write(str(clue_count)+"\n")
    for x in clues:
        f_out.write(str(x[0]) + " " + str(x[1]) + "\n")

