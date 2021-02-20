def solution(m,n,puddles):
    field = [[0]*m for _ in range(0,n)]
    field[0][0]=1
    for j in range(0,m):    # 열
        for i in range(0,n):    # 행
            if i == 0 and j == 0:
                continue
            if [j+1,i+1] in puddles:
                field[i][j]=0
            else:
                if i == 0:
                    field[i][j] = field[0][j-1]
                elif j == 0:
                    field[i][j] = field[i-1][0]
                else:
                    field[i][j] += field[i-1][j]+field[i][j-1]
    answer = field[n-1][m-1]%1_000_000_007
    return answer

if __name__ == "__main__":
    m = 5
    n = 4
    puddles = [[2,2]]   # 행,열 X => 열, 행으로 주어진다
    solution(m,n,puddles)
