function solution(s) {
    let answer = [];
    let arr = s.split("");
    let cnt = 0;


    
    for( i = 0 ; i < arr.length; i++){   
        
        if( arr[i] == " " ){
             answer.push(" ");
             cnt = 0;
            continue;
        }else{
            if( cnt % 2 == 0){
            answer.push( arr[i].toUpperCase())
        }else{
            answer.push(arr[i].toLowerCase())
        }
            cnt++;
        }
        
        
        
        
        
    }
    return answer.join("");
}