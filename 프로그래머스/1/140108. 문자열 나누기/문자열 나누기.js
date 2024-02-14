function solution(s) {
    let xNum = 1;
    let oNum = 0;
    let answer = [];
    
    let arr = s.split("");

    for(i = 1; i < arr.length; i++){
       if( arr[0] == arr[i]){
           xNum++;
       }else{
           oNum++;
       }
        
       if( xNum == oNum ){
           answer.push(s.substring(0,i+1));
           s = s.substring(i+1);
           
           arr.splice(0,i+1)
           
           xNum = 1;
           oNum = 0;
           i = 0;

       } 
        
    }
    if( xNum > 1){answer.push("")}
    
    return  arr.length == 1 || answer.length == 0 ? answer.length+1 : answer.length;
}