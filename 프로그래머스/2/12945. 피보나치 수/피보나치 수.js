function solution(n) {
    let fibo = [0,1];
    let answer = 0;
    
    for(i = 2;i <= n;i++){
        fibo.push((fibo[i-2] + fibo[i-1]) % 1234567)
    }
    answer = fibo[n]
    
    return answer;
}