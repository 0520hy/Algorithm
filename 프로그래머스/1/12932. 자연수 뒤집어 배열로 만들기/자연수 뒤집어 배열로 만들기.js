function solution(n) {
    var arr = [];
    var rev = [];
    
    arr = n.toString().split("");
   
    for(i=0; i < arr.length; i++){
        var num = parseInt(arr[i]);
        
        rev.unshift(num);
    }
      return rev;
   
}