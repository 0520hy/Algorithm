function solution(s) {
    var answer = "";
    if (s.length % 2 == 0){
        var num = s.length/2;
        answer = s.substring(num-1, num+1 )
        
    }else{
        var num = parseInt(s.length/2);
         answer = s.substring(num, num+1 )
}return answer;
    }