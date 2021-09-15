def solution(enter, leave):
    result = [0]*len(leave)
    room=[]
    enter_idx=0
    for l in leave:
        while not l in room:
            room.append(enter[enter_idx])
            enter_idx+=1
        room.remove(l)
        for p in room:
            result[p-1]+=1
        result[l-1]+=len(room)
    return  result