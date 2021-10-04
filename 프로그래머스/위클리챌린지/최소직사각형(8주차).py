def solution(sizes):
    w,h=0,0
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]: sizes[i][0],sizes[i][1]=sizes[i][1],sizes[i][0]
    
    for size in sizes:
        if size[0]>w: w=size[0]
        if size[1]>h: h=size[1]

    return w*h
