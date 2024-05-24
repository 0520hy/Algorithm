function solution(s) {
    let answer = [];
    
    for (let i = 0; i < s.length; i++) {
        let closestIndex = -1;
        
        for (let j = i - 1; j >= 0; j--) {
            if (s[i] === s[j]) {
                closestIndex = i - j;
                break;
            }
        }
        
        answer.push(closestIndex);
    }
    
    return answer;
}
