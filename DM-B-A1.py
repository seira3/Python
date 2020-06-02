
def vd(a,b):
    if a==0 and b==2:
        return -1
    elif a==2 and b==0:
        return 1
    else:
        if a<b:
            return 1
        elif a==b:
            return 0
        else:
            return -1

def preference(vec,num):
    people = [0,1,2]
    people.remove(num)
    ans = 0
    for i in people:
        ans += vd(vec[num],vec[i])
    if ans>0:
        return 2
    elif ans==0:
        return 1
    else:
        return 0

def nash(vec):
    ans = 0
    for i in range(3):
        ans1 = preference(vec,i)
        zyanken = [0,1,2]
        zyanken.remove(vec[i])
        for j in zyanken:
            vec1 = vec[:]
            vec1[i] = j
            if ans1 >= preference(vec1,i):
                ans+=1
    if ans == 6:
        return vec
    else:
        return 0

choice = [0,1,2]
allChoice = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            allChoice.append([choice[i],choice[j],choice[k]])

R = [[[],[],[]],[[],[],[]],[[],[],[]]]

for i in range(3):
    for j in range(27):
        R[i][preference(allChoice[j],i)].append(allChoice[j])

print(R)

nashanswer = []

for i in range(27):
    if nash(allChoice[i]) != 0:
        nashanswer.append(nash(allChoice[i]))
print(nashanswer)

noPareto = [[0,0,2],[0,2,0],[2,0,0],[0,1,1],[1,0,1],[1,1,0],[1,2,2],[2,1,2],[2,2,1]]

for i in noPareto:
    paretoAnswer = allChoice[:]
    paretoAnswer.remove(i)

print(paretoAnswer)

