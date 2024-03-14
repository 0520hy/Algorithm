function solution(s){
    let answer = true;
    let cnt = 0;
    
    for(i=0; i<s.length; i++){
        if(s[i] == "(" ){
            cnt ++;
        }if(s[i] == ")" ){
            cnt --;
        }if(cnt < 0){
            answer = false;
            break;
        }else{
             cnt == 0 ? answer = true : answer = false;
        }
        }
   
    
  

    return answer;
}