def solution():
    arr = [1,9,2,7,5,6,9,2,8,2]
    N=len(arr)
    W=3
    S=[0]*(N-W)
    for i in range(W): S[0]+=arr[i]
    for i in range(1,N-W):
        S[i]=S[i-1]-arr[i-1]+arr[i+W-1]
    print(S) #[12, 18, 14, 18, 20, 17, 19]

solution()