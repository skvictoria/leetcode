'''
# set bin
bin - > [0 0 0 0 0 0 0 0] (0~height_bin)
# 
for i in rectangles:
    for left to right:
        maxv = max(maxv, bin[left] + cur_height)
    bin[left:right] = maxv
    res[i] = [rectangles[i][0], maxv-cur_height, rectangles[i][2], maxv]
'''


def solution(rectangles):
    # set bin
    height_bin = 0
    for i in range(len(rectangles)):
        height_bin = max(height_bin, rectangles[i][2])
    bin = [0]*(height_bin)

    # move to down
    down = [[0]*4 for _ in range(len(rectangles))]
    for i in range(len(rectangles)):
        height = rectangles[i][3] - rectangles[i][1]
        left = rectangles[i][0]
        right = rectangles[i][2]
        maxv = 0
        for span in range(left, right):
            maxv = max(maxv, bin[span] + height)
        for span in range(left, right):
            bin[span] = maxv
        down[i] = [left, maxv-height, right, maxv]

    # set bin
    width_bin = 0
    for i in range(len(down)):
        width_bin = max(width_bin, down[i][3])
    bin = [0]*(width_bin)

    # move to left
    left = ["" for _ in range(len(down))]
    for i in range(len(down)):
        width = down[i][2] - down[i][0]
        upside = down[i][3]
        downside = down[i][1]
        maxv = 0
        for span in range(downside, upside):
            maxv = max(maxv, bin[span]+width)
        for span in range(downside, upside):
            bin[span] = maxv
        left[i] = "{} {} {} {}".format(maxv-width, downside, maxv, upside)
    
        
    return left