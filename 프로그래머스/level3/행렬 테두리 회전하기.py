def rotate(matrix, query, result):
    x1,y1,x2,y2 = query
    x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
    minVal = float('inf')

    tmp=matrix[x1][y2]
    minVal = min(tmp,minVal)
    #상
    for i in range(y2,y1,-1):
        matrix[x1][i] = matrix[x1][i-1]
        minVal = min(matrix[x1][i],minVal)
    #좌
    for i in range(x1,x2):
        matrix[i][y1] = matrix[i+1][y1]
        minVal = min(matrix[i][y1],minVal)
    #하
    for i in range(y1,y2):
        matrix[x2][i] = matrix[x2][i+1]
        minVal = min(matrix[x2][i+1],minVal)
    #우
    for i in range(x2,x1,-1):
        matrix[i][y2] = matrix[i-1][y2]
        minVal = min(matrix[i][y2],minVal)
    matrix[x1+1][y2]=tmp

    result.append(minVal)

def solution(rows, columns, queries):
    matrix = [[0]*columns for _ in range(rows)]
    cnt=1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j]=cnt
            cnt+=1

    result = []
    for query in queries:
        rotate(matrix, query, result)
    return result

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
