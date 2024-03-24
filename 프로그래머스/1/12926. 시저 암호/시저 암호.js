function solution(s, n) {
    var answer = [];
    let arr = s.split("")
    
    for ( i = 0; i < s.length; i++){
        let num = arr[i].charCodeAt();
        
      if( 65 <= num && 90 >= num ){
          answer.push(String.fromCharCode((num + n - 65) % 26 + 65))
         
      }else if( 97 <= num && 122 >= num ){
       answer.push(String.fromCharCode((num + n - 97) % 26 + 97)) 
           
    }else{
        answer.push(" ");
     
    }
    
    }
    return answer.join("");
}