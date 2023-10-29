import numpy as np

vertex = 6
INF = 1000000
                #   1    2    3  4  5    6
arr_di = np.array([[0  , 2  , 5, 1, INF, INF],
                   [2  , 0  , 3, 2, INF, INF],
                   [5  , 3  , 0, 3, 1  , 5],
                   [1  , 2  , 3, 0, 1  , 2],
                   [INF, INF, 1, 1, 0  , 2],
                   [INF, INF, 5, INF, 2, 0]])

visit_flag = np.zeros((vertex))
result_dist = np.zeros((vertex))

def dijkstra():
    # start with 0
    i = 0
    visit_flag[i] = True
    # update result_dist for 0
    for j in range(vertex):
        result_dist[j] = arr_di[i][j]

    # until the flag has false,
    while(np.sum(visit_flag) < 6):
        # find the minimum route that I did not go so far
        min = INF
        idx = i
        for j in range(0, vertex):
            if((i == j) or (visit_flag[j] == True)):
                continue
            else:
                if(min > arr_di[i][j]):
                    min = arr_di[i][j]
                    idx = j
        # update the flag
        visit_flag[idx] = True

        # update the result_dist for that index
        for j in range(vertex):
            # compare
            if(arr_di[idx][j] + result_dist[idx] < result_dist[j]):
                result_dist[j] = arr_di[idx][j] + result_dist[idx]

dijkstra()
print(result_dist)