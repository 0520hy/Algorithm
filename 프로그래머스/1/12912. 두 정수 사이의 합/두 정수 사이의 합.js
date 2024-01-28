function solution(a, b) {
    
    var answer = 0;
    var x = 0;
    var y = 0;
    
    if (a < b) {
        x = a;
        y = b;
    }else {
        x = b;
        y = a;
    }
    
    for ( i = x; x <= y ; x++){
         answer += x;
        
    }
    return answer
}