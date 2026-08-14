import sys
file = sys.stdin # input
row=0
mRow, mCol = 0,0

global_maxx = 0
for line in file :
    col =0
    row +=1
    lines = line.split("\t")
    line_nums = [] 

    for s in lines:
        line_nums.append(float(s))
    curr_max= line_nums[0]

    for i in line_nums:
        col+=1
        if curr_max < i:
            curr_max = i
            mCol = col 
    

    if global_maxx < curr_max:
        global_maxx = curr_max
        mRow = row

print(mRow, mCol,  global_maxx)


    
    