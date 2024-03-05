function solution(s) {
    let answer = [];    
    let arr = s.split(" ");
    
    answer.push(Math.min(...arr));
    answer.push(" ");
    answer.push(Math.max(...arr));
    
    return answer.join("");
}