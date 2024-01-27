function solution(n) {
     
    var arr = n.toString().split("");
    
    arr.sort().reverse();
    var answer = Number(arr.join(""));
    return answer;
        
    
}