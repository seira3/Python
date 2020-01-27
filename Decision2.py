import math

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

def decision3(x):
    count = 0
    x1 = x[0][2] + x[1][1] + x[2][2]
    x2 = x[0][0] + x[1][2] + x[2][0]
    x3 = x[0][1] + x[1][0] + x[2][1]
    point = sorted([x1,x2,x3])
    if point[-1] != point[1]:
        return 1
    else:
        return 0

def pattern(dataset,addpatterner,maxpoint):
    patternnumber = 1
    for i in range(3):
        if addpatterner[i] == [0,0,0]:
            gap = maxpoint - dataset[i][0]
        elif addpatterner[i] == [1,0,0]:
            gap = dataset[i][0] - dataset[i][1] + 1
        elif addpatterner[i] == [1,1,0]:
            gap = dataset[i][1] - dataset[i][2] + 1
        elif addpatterner[i] == [1,1,1]:
            gap = dataset[i][2] - 1
        patternnumber = patternnumber * math.factorial(gap) * (gap + 1)
    return patternnumber

def case1(dataset,maxpoint):
    OKcount = 0
    NGcount = 0
    newdataset = []
    for k in range(len(dataset)):
        for m in range(64):
            addvalue = pattern(dataset[k],addpattern[m],maxpoint)
            c = listsum(dataset[k],addpattern[m])
            if decision1(c) == 1:
                OKcount += addvalue
            else:
                NGcount += addvalue
                newdataset.append(c)
    prob = OKcount / (OKcount + NGcount)
    return [OKcount,NGcount,newdataset,prob]

def case2(dataset,maxpoint):
    OKcount = 0
    NGcount = 0
    newdataset = []
    for k in range(len(dataset)):
        for m in range(64):
            addvalue = pattern(dataset[k],addpattern[m],maxpoint)
            c = listsum(dataset[k],addpattern[m])
            if decision2(c) == 1:
                OKcount += addvalue
            else:
                NGcount += addvalue
                newdataset.append(c)
    prob = OKcount / (OKcount + NGcount)
    return [OKcount,NGcount,newdataset,prob]

def case3(dataset,maxpoint):
    OKcount = 0
    NGcount = 0
    newdataset = []
    for k in range(len(dataset)):
        for m in range(64):
            addvalue = pattern(dataset[k],addpattern[m],maxpoint)
            c = listsum(dataset[k],addpattern[m])
            if decision3(c) == 1:
                OKcount += addvalue
            else:
                NGcount += addvalue
                newdataset.append(c)
    prob = OKcount / (OKcount + NGcount)
    return [OKcount,NGcount,newdataset,prob]

value4 = case1(ivalue,3)[2]
value5 = case1(value4,4)[2]
value6 = case1(value5,5)[2]
value7 = case1(value6,6)[2]

print(case1(ivalue,3)[3])
print(case1(value4,4)[3])
print(case1(value5,5)[3])
print(case1(value6,6)[3])
print(case1(value7,7)[3])
