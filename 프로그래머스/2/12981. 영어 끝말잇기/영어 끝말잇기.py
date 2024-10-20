# for문 돌면서 이전에 나온 단어인지, 앞 단어의 뒤 글자와 같은지 확인

# 번호 -> 다르면 해당 단어의 인덱스 % 사람 수
# 차례 -> 인덱스 / 사람수
# [번호, 차례]


def solution(n, words):
    answer = []
    tmp = []
    lastword = ''

    
    for i in range(len(words)):

        if words[i] in tmp or (lastword and not words[i].startswith(lastword)):
            answer.append(i % n + 1 )
            answer.append(i // n + 1)

            return answer
        
        else:
            tmp.append(words[i])
            lastword = words[i][-1]

    return [0,0]