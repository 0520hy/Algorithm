function solution(food) {
    var answer = '';
    
    for( i = 1; i < food.length; i++){
        let num = food[i] / 2;
        for( k = 1; k <= num; k++){
            answer += i
        }
    }
    
     let reverse = answer.split("").reverse().join("");
     answer += "0"
     answer += reverse
    
    return answer;
}