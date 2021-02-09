import sys
import heapq
def search(n,timeList):
    timeheap = [timeList[0][1]]

    for i in range(1,n):
        if timeList[i][0] < timeheap[0]:
            heapq.heappush(timeheap,timeList[i][1])
        else:
            heapq.heappop(timeheap)
            heapq.heappush(timeheap,timeList[i][1])
    print(len(timeheap))

if __name__ == "__main__":
    timeList = []
    n = int(sys.stdin.readline())   #int(input())
    for _ in range(0, n):
        s, t = map(int, sys.stdin.readline().split())   #map(int, input().split())
        timeList.append([s,t])
    timeList.sort(key=lambda x: x[0]) # 시작 시간을 기준으로 오름차순 정렬
    search(n,timeList)