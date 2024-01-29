function solution(phone_number) {
    var arr = phone_number.split("");
    
    for (i=0; i < arr.length-4; i++){
        arr[i] = "*";
    }
    
    
   return arr.join("")
}