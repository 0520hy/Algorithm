function solution(x) {
   var arr = x.toString().split("");
    var sum = 0;


    for(i = 0; i < arr.length; i++){
        sum +=  Number(arr[i]);
    }
   if (x % sum == 0) return true;
    else return false;
}