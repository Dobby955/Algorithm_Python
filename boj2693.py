x = int(input())
for i in range(x):
    nums = list(map(int, input().split()))
    nums = sorted(nums)
    print(nums[-3])
    
    