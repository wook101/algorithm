def recursion(collection,tmp,cnt,dictionary):
    for i in range(5):
        if len(tmp)==5: return
        tmp.append(collection[i])
        cnt[0]+=1
        dictionary[''.join(tmp)] = cnt[0]
        recursion(collection,tmp,cnt,dictionary)
        tmp.pop()

def solution(word):
    dictionary={}
    recursion(["A","E","I","O","U"], [], [0], dictionary)
    return dictionary[word]

solution("AAAAE")	#6
solution("AAAE")	#10
solution("I")	    #1563
solution("EIO") 	#1189