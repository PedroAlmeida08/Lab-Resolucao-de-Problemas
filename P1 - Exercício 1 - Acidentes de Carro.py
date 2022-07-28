ret1_x0, ret1_y0, ret1_x1, ret1_y1 = input().split()
ret1_x0 = int(ret1_x0)
ret1_y0 = int(ret1_y0)
ret1_x1 = int(ret1_x1)
ret1_y1 = int(ret1_y1)
ret2_x0, ret2_y0, ret2_x1, ret2_y1 = input().split()
ret2_x0 = int(ret2_x0)
ret2_y0 = int(ret2_y0)
ret2_x1 = int(ret2_x1)
ret2_y1 = int(ret2_y1)
if (((ret2_x0 > ret1_x0 and ret2_x0 > ret1_x1) and (ret2_y0 > ret1_y0 and ret2_y0 > ret1_y1) and
     (ret2_x1 > ret1_x0 and ret2_x1 > ret1_x1) and (ret2_y1 > ret1_y0 and ret2_y1 > ret1_y1)) or
    ((ret2_x0 < ret1_x0 and ret2_x0 < ret1_x1) and (ret2_y0 < ret1_y0 and ret2_y0 < ret1_y1) and
     (ret2_x1 < ret1_x0 and ret2_x1 < ret1_x1) and (ret2_y1 < ret1_y0 and ret2_y1 < ret1_y1))):
    result = 0
else:
    result = 1
print(result)
