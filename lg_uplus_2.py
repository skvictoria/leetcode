'''
hash = {0:0, v[0][1]:1}
line = [0]*len(dist)
line[1] = v[0][1]
for i in range(2, len(dist)):
    x = v[0][i]
    y = v[1][i]
    if y != x+line[1]:
        line[i] = x
        hash{x:i}
    else:
        line[i] = -x
        hash{-x:i}


'''

def solution(dist):
    answer = dist[:2]
    hash = {0:0, dist[0][1]:1}
    
    for i in range(2, len(dist)):
        x = dist[0][i]
        y = dist[1][i]
        if y != x+dist[0][1]:
            hash[x] = i
        else:
            hash[-x] = i
    i = 0
    for key, value in sorted(hash.items()):
        answer[0][i] = value
        i += 1
    for i in range(1, len(answer[0])):
        answer[1][i-1] = answer[0][-i]
    answer[1][len(answer[0])-1] = answer[0][0]
    
    return sorted(answer)