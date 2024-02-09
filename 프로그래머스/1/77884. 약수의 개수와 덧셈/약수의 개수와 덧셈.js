function solution(left, right) {
    
    let cnt = 0;
    let even = 0;
    let odd = 0;
    
    for(i = left; i <= right; i++){
        for(j = 1; j <= i; j++){
            if(i % j == 0) {
                cnt ++
            } 
        }
        cnt % 2 == 0 ? even +=  i : odd += i;
        cnt = 0;
    }
     return even - odd;
}