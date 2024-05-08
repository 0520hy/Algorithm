function solution(strlist) {
    var answer = [];
    
    for(i = 0; i <strlist.length; i++){
        let len = strlist[i].split("").length;
        answer.push(len)
    }
    return answer;
}