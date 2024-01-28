function solution(s){
    
    var pNum = 0;
    var yNum = 0;
    
    var arr = s.split("");
    
    for(i=0; i<arr.length; i++){
        if("p" === arr[i].toLowerCase()){
            pNum++;
        } if("y" === arr[i].toLowerCase()){
            yNum++;
        }
    }
    if (pNum == yNum){
        return true;
    }else{
        return false;
    }
    
}