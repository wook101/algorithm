from collections import defaultdict
default_dic = defaultdict(int)
keys = ["a","b","d","e","t","a","e"]
for key in keys:
    default_dic[key]+=1
print(default_dic)
#dfault_dic에서 key에 대한 값을 조회했을 때 값이없는 경우, int일때 0으로 초기화