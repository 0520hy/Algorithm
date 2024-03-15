function solution(s) {
    let answer =[]
    let tmp = '';
    let zero = 0;
    let cnt = 0;
    
    while(s !== '1'){
        
       tmp = s.replace(/0/g,'');
        console.log("tmp=", tmp)
        zero += (s.length - tmp.length);
        console.log("zero=", zero)
        s = tmp.length.toString(2);
        console.log("s=", s)
        cnt++
        
     
    }
          
    answer = [cnt, zero]
     return answer;
}