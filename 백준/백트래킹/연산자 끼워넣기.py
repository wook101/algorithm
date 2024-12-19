import sys
def recursive(num, idx, add, sub, mul, div):
    global minValue, maxValue
    if idx == n:
        maxValue = max(maxValue, num)
        minValue = min(minValue, num)
        return

    if add > 0:
        recursive(num + nums[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        recursive(num - nums[idx], idx + 1 ,add, sub - 1, mul, div)
    if mul > 0:
        recursive(num * nums[idx], idx + 1, add, sub, mul - 1, div)
    if div > 0:
        recursive(int(num / nums[idx]), idx + 1, add, sub, mul, div - 1)

n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
maxValue = -sys.maxsize
minValue = sys.maxsize
def solution():
    recursive(nums[0], 1, op[0], op[1], op[2], op[3])
    print(maxValue)
    print(minValue)
solution()