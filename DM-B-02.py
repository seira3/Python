def pareto(vecvec,subjectNum):
    num = len(vecvec)
    ans = []
    for i in range(num):
        numnum = list(range(num))
        numnum.remove(i)
        ansCount = 0
        for j in numnum:
            count = 0
            equalCount = 0
            for k in range(subjectNum):
                if vecvec[i][k] < vecvec[j][k]:
                    count += 1
                elif vecvec[i][k] == vecvec[j][k]:
                    count += 1
                    equalCount += 1
            if count == subjectNum and equalCount != subjectNum:
                ansCount += 1
                break
        if ansCount == 0:
            ans.append(vecvec[i])
    return ans

Q2_2_3 = [[4,9,6],[3,2,2],[8,4,8],[7,8,3],[5,6,7],[2,1,4],[9,3,9],[6,7,5],[1,5,1]]
Q2_2_4 = [[5,5,5],[6,10,3],[3,8,2],[2,9,6],[1,6,9],[4,1,1],[8,7,10],[9,2,7],[10,4,4],[7,3,8]]


print(pareto(Q2_2_3,3))
print(pareto(Q2_2_4,3))
