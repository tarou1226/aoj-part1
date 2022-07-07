while True:
    height, width = map(int, input().split())
    if height and width == 0:
        break
    for i in range(height):
        for j in range(width):
            if i == 0 or j == 0 or i == height - 1 or j == width - 1:
                print("#", end = "")
            else:
                print("・", end = "")
        print()