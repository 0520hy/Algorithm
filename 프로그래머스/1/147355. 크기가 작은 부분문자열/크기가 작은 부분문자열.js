function solution(t, p) {
    var answer = 0;
    
    let tmp = [];
    
    for( i = 0; i<t.length; i++){
        tmp.push(t.slice(i, i + p.length ));

    }
    console.log(tmp)
    for( i = 0; i<tmp.length; i++){
        if(tmp[i].length == p.length){
            tmp[i] <= p ? answer++ : "";
        }
    }
    return answer;
    
   
    
    
    
}