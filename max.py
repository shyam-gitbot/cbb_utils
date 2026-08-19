import sys
file = sys.stdin # input
row,mRow, mCol,global_maxx = 0,0,0,float('-inf')

for line in file :
    col =0
    row +=1
    lines = line.split("\t")

    curr_col=1
    curr_max= float(lines[0])

    for i in lines:
        col+=1
        if curr_max < float(i):
            curr_max = float(i)
            curr_col = col

    if global_maxx < curr_max:
        global_maxx = curr_max
        mRow = row
        mCol = curr_col

print(mRow, mCol,  global_maxx)


    
    