addpoint = [[0,0,0],[1,0,0],[1,1,0],[1,1,1]]

addpattern = [0]*64

ivalue = [[[3,2,1],[3,2,1],[3,2,1]]]

count = 0

for i in range(4):
    a = [0,0,0]
    a[0] = addpoint[i]
    for j in range(4):
        a[1] = addpoint[j]
        for k in range(4):
            a[2] = addpoint[k]
            b = a[::]
            addpattern[count] = b
            count+=1

def listsum(x,y):
    a = [0,0,0]
    for i in range(3):
        b = [0,0,0]
        for j in range(3):
            b[j] = x[i][j] + y[i][j]
        a[i] = b
    return a

def decision1(x):
    count = 0
    x1 = x[0][0] + x[1][2] + x[2][1]
    x2 = x[0][1] + x[1][0] + x[2][2]
    x3 = x[0][2] + x[1][1] + x[2][0]
    point = sorted([x1,x2,x3])
    if point[-1] != point[1]:
        return 1
    else:
        return 0

def decision2(x):
    count = 0
    x1 = x[0][2] + x[1][1] + x[2][0]
    x2 = x[0][1] + x[1][0] + x[2][2]
    x3 = x[0][0] + x[1][2] + x[2][1]
    point = sorted([x1,x2,x3])
    if point[-1] != point[1]:
        return 1
    else:
        return 0


def case1(dataset):
    count = 0
    newdataset = []
    for k in range(len(dataset)):
        for m in range(64):
            c = listsum(dataset[k],addpattern[m])
            if decision1(c) == 1:
                count += 1
            else:
                newdataset.append(c)
    prob = count/(count+len(newdataset))
    return [count,newdataset,prob]

def case2(dataset):
    count = 0
    newdataset = []
    for k in range(len(dataset)):
        for m in range(64):
            c = listsum(dataset[k],addpattern[m])
            if decision2(c) == 1:
                count += 1
            else:
                newdataset.append(c)
    prob = count/(count+len(newdataset))
    return [count,newdataset,prob]

value4 = case1(ivalue)[1]
value5 = case1(value4)[1]
value6 = case1(value5)[1]
value7 = case1(value6)[1]
"""
Value4 = case2(ivalue)[1]
Value5 = case2(Value4)[1]
Value6 = case2(Value5)[1]
Value7 = case2(Value6)[1]
"""
print(case1(ivalue)[2])
print(case1(value4)[2])
print(case1(value5)[2])
print(case1(value6)[2])
#print(case1(value7)[2])
