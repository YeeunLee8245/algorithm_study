def solution(genres, plays):
    answer = []
    dic = {}
    overCnt = 0
    orderList=[]
    num = 0
    maxStr = ""
    maxIdx = 0
    sumCnt = 0
    singleCnt = 0
    genresCntDic = {}
    for idx, name in enumerate(genres):
        if name in dic:
            dic[name] += plays[idx]
            continue
        dic[name] = plays[idx]
    for name in dic:    # 장르에 속한 곡이 하나인 것에 유의하자
        if 1 < genres.count(name):
            genresCntDic[name]=2
            overCnt += 2
            continue
        else:
            singleCnt += 1
            genresCntDic[name]=1
    while dic:
        for name in dic:
            if num < dic[name]:
                num = dic[name]
                maxStr = name
        num = 0
        orderList.append(maxStr)
        del dic[maxStr]
    while True:
        for idx, genre in enumerate(genres):
            if orderList[0] == genre:
                if num < plays[idx]:
                    num = plays[idx]
                    maxIdx = idx
        answer.append(maxIdx)
        sumCnt += 1
        plays[maxIdx] = 0
        num = 0
        if sumCnt == genresCntDic[orderList[0]]:
            orderList.pop(0)
            sumCnt = 0
        if len(answer) == overCnt+singleCnt:
            break
    return answer

genres = ["classic","pop","classic","classic","pop"]
plays = [500,600,150,800,2500]

solution(genres,plays)