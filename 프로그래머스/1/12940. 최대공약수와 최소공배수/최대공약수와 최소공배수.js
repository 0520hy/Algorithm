function solution(n, m) {
    let maxNum = 0;
    let minNum = 0;
    
    var answer = [];
    
    for( i = 1; i <= Math.max(n,m); i++){
        if(n % i == 0 && m % i == 0){
            maxNum = i;
        }
    }
    
    answer.push(maxNum);
    answer.push(n*m/maxNum);
    
    return answer;
}