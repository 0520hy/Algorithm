function solution(food) {
    var answer = '';
    
    for( i = 1; i < food.length; i++){
        let num = i.toString();
        answer += num.repeat((food[i] / 2))
       
        // for( k = 1; k <= num; k++){
        //     answer += i
        // }
    }
    
     let reverse = answer.split("").reverse().join("");
     answer = answer + "0" + reverse;
    
    return answer;
}