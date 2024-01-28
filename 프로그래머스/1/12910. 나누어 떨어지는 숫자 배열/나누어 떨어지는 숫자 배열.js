function solution(arr, divisor) {
    var answer = [];
     for(i=0; i<arr.length; i++){
         if(arr[i] % divisor == 0){
             answer.push(arr[i]);
         }
       
     }
        if (answer == ""){
            answer = [-1];
            return answer;
        }else{
           answer = answer.sort((a,b) => a-b)
            return answer;
                      }
        }
    
    
    
