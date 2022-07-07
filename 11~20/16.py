n = int(input())
lists = list(map(int, input().split()))

if len(lists) > n:
    print("error")
else:   
    ans_min = min(lists)
    ans_max = max(lists)
    ans_sum = sum(lists)
    print("{0} {1} {2}".format(ans_min, ans_max, ans_sum))