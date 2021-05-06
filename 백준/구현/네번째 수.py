nums=list(map(int,input().split()))
nums.sort()
res=0
d1=nums[1]-nums[0]
d2=nums[2]-nums[1]
res = nums[-1]+d1 if d1==d2 else nums[0]+d2 if d1>d2 else nums[-1]-d1
print(res)

