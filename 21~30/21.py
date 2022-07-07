n = int(input())

lists = list(map(int, input().split()))

if n < len(lists):
    print("error")
else:
    lists.reverse()
    print(lists)