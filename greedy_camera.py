def solution(routes):
    answer = 1
    routes.sort(key= lambda x: x[0])
    s= routes[0][0]
    t = routes[0][1]
    for i in range(1,len(routes)):
        if t < routes[i][0] or s > routes[i][1]:
            s = routes[i][0]
            t = routes[i][1]
            answer += 1
        else:
            if s <= routes[i][0]:
                s = routes[i][0]
                if t >= routes[i][1]:
                    t= routes[i][1]
        #print(answer)
        #print(s,t)
    return answer

if __name__=="__main__":
    solution([[-20,15],[-14,-5],[-18,-13],[-5,-3]])