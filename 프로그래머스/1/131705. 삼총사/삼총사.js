function solution(number) {
    let answer = 0;
    let sum = 0;
    
    for(i=0; i<number.length; i++){
        for(j=0; j<number.length; j++){
            for(k=0; k<number.length; k++){
                if( i !== j && j !== k && i !== k){
                    if(number[i] + number[j] + number[k] == 0 ){
                        answer ++;
                    }
                }
            }
        }
    }
    return answer/6;
}