function solution(s) {
    var arr = "";
    arr = s.split("");
     var lower = [];
    var upper = []
    for ( i = 0; i <arr.length; i++){
        if(arr[i] == arr[i].toLowerCase()){
            lower.push(arr[i]);
            lower.sort().reverse();
        }else{
            upper.push(arr[i]);
            upper.sort().reverse();
        }
    } var answer = lower.concat(upper);
    return answer.join("")
    
}