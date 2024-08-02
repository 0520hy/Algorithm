from itertools import product

def solution(word):

    dic = []
    vow = ['A', 'E', 'I','O', 'U']
    
    for i in range(1, 6):
        for wd in product(vow, repeat = i):
            dic.append(''.join(wd))
    dic.sort()
     
    return dic.index(word) +1