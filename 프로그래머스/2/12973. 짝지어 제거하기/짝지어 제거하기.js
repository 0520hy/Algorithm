function solution(s) {

    let arr = [];
    
    if(s.length  % 2 == 1 ) return 0
    
    for(i = 0; i < s.length; i++){
        if( s[i] == arr[arr.length - 1]){
            arr.pop();
        }else{
            arr.push(s[i])
        }
        
        
    }

   return arr.length == 0 ? 1 : 0;
    
}
