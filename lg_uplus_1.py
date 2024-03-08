def bfs(v_val, u_val, v, checked):
    area = 1
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    for i in range(4):
        v_new = v_val + dy[i]
        u_new = u_val + dx[i]
        if 0<=v_new<len(v) and 0<=u_new<len(v[0]) and v[v_new][u_new]==1 and checked[v_new][u_new]==0:
            checked[v_new][u_new] = 1
            area += bfs(v_new, u_new, v, checked)
    return area

def solution(v):
    width = len(v[0])
    height = len(v)
    max_area = 0
    num_of_white = 0
    checked = [[False]*width for _ in range(height)]
    for v_val in range(height):
        for u_val in range(width):
            if v[v_val][u_val] == 1 and checked[v_val][u_val] == 0:
                checked[v_val][u_val] = 1
                max_area = max(max_area, bfs(v_val, u_val, v, checked))
                num_of_white += 1
    return [num_of_white, max_area]