import sys

def encode(strings):
    if strings == None or len(strings)==0:
        return ""
    prev_chr = ""
    res = []
    counter = 0
    for cur_chr in strings:
        if cur_chr == prev_chr:
            counter += 1
        elif prev_chr == "":
            prev_chr = cur_chr
            counter = 1
        else:
            res.append(prev_chr+str(counter))
            prev_chr = cur_chr
            counter = 1
    return res

input = sys.stdin.readline
strings = str(input())
print(encode(strings))