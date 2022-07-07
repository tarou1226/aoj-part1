mark = "SHCD"

cards = [[False for _ in range(14)] for _ in range(4)]

n = int(input())

for i in range(n):
    s, num = input().split()
    num = int(num)
    cards[mark.find(s)][num] = True

for i in range(4):
    for j in range(1, 14):
        if not cards[i][j]:
            print(mark[i], j)