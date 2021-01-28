def solution(cityNum,busList):
    routeLi = [[inf]*cityNum for _ in range(0,cityNum)]
    for s,e,v in busList:
        if routeLi[s-1][e-1] > v:
            routeLi[s-1][e-1] = v
    for i in range(0,cityNum):
        routeLi[i][i]= 0
    for m in range(0,cityNum):
        for s in range(0,cityNum):
            for e in range(0,cityNum):
                if routeLi[s][e] > routeLi[s][m]+routeLi[m][e]:
                    routeLi[s][e] = routeLi[s][m]+routeLi[m][e]
    for route_i in routeLi:
        for j in range(0,len(routeLi)):
            if route_i[j] == inf:
                route_i[j] = 0
                print(route_i[j],end=' ')
                print(sep="\n")

if __name__=="__main__":
    inf = 20000000 # 100000*100 이상
    cityNum = int(input())
    busNum = int(input())
    li = [[0, 0, 0] for _ in range(0, busNum)]
    for i in range(0,busNum):
        start, end, value = map(int, input().split())
        li[i][0]= start
        li[i][1]= end
        li[i][2]= value
    solution(cityNum,li)