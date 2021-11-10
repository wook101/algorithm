def solution():
  N = int(input())
  arr = [int(input()) for _ in range(N)]
  arr.sort()

  hacker = 0
  count=1
  for i in range(len(arr)):
      if arr[i] < count: continue
      if arr[i] > count:
          hacker += arr[i]-count
      count+=1
      
  return hacker
