while True:
    height, width = map(int, input().split())
    ans = 0
    if height and width == 0:
        break
    for i in range(height):
        for j in range(width):
            if (i + j) % 2 == 0:
                print("#", end = "")
            else:
                print(".", end = "")
            ans += 1
        print()