
function solution(absolutes, signs) {
    
    var sum = 0;
    
  for(i=0; i < absolutes.length; i++){
      if(signs[i] === true){
          sum += (absolutes[i]);
      }else{
          sum += (absolutes[i]*-1)
      }
  }
    return sum;
}