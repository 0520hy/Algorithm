def solution(myStr):
    sp = ["a","b","c"]
    
    for i in myStr:
        if i in sp:
            myStr = myStr.replace(i, " ")
            
    return ["EMPTY"] if len(myStr.split()) == 0 else myStr.split()