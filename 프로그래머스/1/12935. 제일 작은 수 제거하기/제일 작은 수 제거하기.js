function solution(arr) {
     var answer = [];
    if ( arr.length !== 1){
        const minVal = Math.min(...arr);
        answer = arr.filter((n) => n !== minVal);
        
    }else {
        answer.push(-1)
    }return answer
}