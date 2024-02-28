function solution(numbers) {
    var answer = [];
    
    for( i = 0; i < numbers.length; i++){
        for( j = 0; j < numbers.length; j++){
            if(i !== j){
                answer.push(numbers[i] + numbers[j]);
            }
        }
    }
    
    answer = [...new Set(answer)];
    
    
    return answer.sort((a,b)=>a-b);
}