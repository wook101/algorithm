def solution(n):
    arr, ans = ['4', '1', '2'], ""
    while n>0:
        mod = n%3
        ans = arr[mod]+ans
        if mod==0:
            n=n//3-1
        else:
            n=n//3
    return ans
print(solution(10))

