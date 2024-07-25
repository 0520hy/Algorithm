def solution(myString, pat):
    last = myString.rfind(pat)

    return myString[:last + len(pat)]