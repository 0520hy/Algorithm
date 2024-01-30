function solution(n) {
    var answer = [];
   
    for(var i=0;i<n;i++){
       
        if (i % 2 == 0){
            answer.push("수");
             
        }else{
             answer.push("박");
        }
    }return answer.join("");
}