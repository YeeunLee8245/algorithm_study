def solution(begin, target, words):
    answer = 0
    stack = []
    diffLi = [100 for _ in range(0,len(words))]
    current = begin
    diffCnt = 0
    moveWords = list(words)

    if target not in words:
        return 0
    stack.append(begin)
    while True:
        if stack[-1] == target:
            break
        if len(stack) == 0:
            return 0
        removeWord = stack.pop()
        if removeWord in moveWords:
            moveWords[moveWords.index(removeWord)]=""
        for idx,word in enumerate(moveWords):  # diffLi 갱신
            for i in range(0,len(word)):
                if current == word or word =="":
                    diffCnt = 100
                    break
                if current[i] != word[i]:
                    diffCnt += 1
                continue
            diffLi[idx] = diffCnt
            diffCnt = 0
        if 1 < min(diffLi):
            return 0
        for idx,cnt in enumerate(diffLi):
            if cnt == 1:
                stack.append(words[idx])
        answer += 1
        current = stack[-1]

    return answer

li =  ["cog", "log", "lot", "dog", "dot", "hot"] #["hot", "dot", "dog", "lot", "log", "cog"]
solution("hit","cog",li)