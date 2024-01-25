function solution(n)
{
    
   
    var arr = n.toString().split("");
    var sum = 0;
  
    for(i=0; i < arr.length; i++){
          sum += Number(arr[i]);
    }
          return sum;

    
}