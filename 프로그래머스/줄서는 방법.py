'''
n	k	result
3	5	[3,1,2]
'''
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def solution(n, k):
    result = []
    nums = [i + 1 for i in range(n)]
    x = factorial(n) // n
    j = -1

    while True:
        idx = (k - 1) // x
        result.append(nums[idx])
        nums.remove(nums[idx])
        if not nums:
            break
        k = k % x
        x = x // (n + j)
        j -= 1

    return result