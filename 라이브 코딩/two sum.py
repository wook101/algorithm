'''
합이 n이 되는 두개의 원소의 인덱스 찾기
'''

def solution(arr,n): #시간복잡도 O(n), 공간복잡도 O(n)
    data = {}  #key - 숫자, value - 인덱스,
    for idx in range(len(arr)):
        if n-arr[idx] in data:
            return [data[n-arr[idx]], idx]
        else:
            data[arr[idx]] = idx

    return None

print(solution([1,5,2,6,8,10,4,9,3,12], 7))