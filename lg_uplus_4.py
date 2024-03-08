'''
right = image[:]
for v in range(len(image)):
    for u in range(len(image[0])):
        right[v][u] = image[v][-(u+1)]

down = image[:]
for v in range(len(image)):
    for u in range(len(image[0])):
        down[v][u] = image[-(v+1)][u]

right_down = image[:]
for v in range(len(image)):
    for u in range(len(image[0])):
        right_down[v][u] = down[v][-(u+1)]
'''

def solution(image):
    answer = [[0]*(len(image)*2) for _ in range(len(image)*2)]
    right = [[0]*(len(image)) for _ in range(len(image))]
    for v in range(len(image)):
        for u in range(len(image[0])):
            right[v][u] = image[v][-(u+1)]
    
    down = [[0]*(len(image)) for _ in range(len(image))]
    for v in range(len(image)):
        for u in range(len(image[0])):
            down[v][u] = image[-(v+1)][u]

    right_down = [[0]*(len(image)) for _ in range(len(image))]
    for v in range(len(image)):
        for u in range(len(image[0])):
            right_down[v][u] = down[v][-(u+1)]
    for v in range(0, len(image)):
        for u in range(0, len(image[0])):
            answer[v][u] = image[v][u]
            answer[v+len(image)][u] = down[v][u]
            answer[v][u+len(image)] = right[v][u]
            answer[v+len(image)][u+len(image)] = right_down[v][u]
    
    return answer