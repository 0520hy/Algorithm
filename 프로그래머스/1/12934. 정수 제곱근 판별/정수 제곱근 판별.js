function solution(n) {
  
    
    var squ = Math.sqrt(n);
    if(Number.isInteger(squ)){
        return (squ+1) * (squ+1);
    }else{
        return -1;
    }
    
}