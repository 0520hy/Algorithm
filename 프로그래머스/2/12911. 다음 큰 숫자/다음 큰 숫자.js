function solution(n) {
    let answer = 0;
    let tmp = n.toString(2);
    const num = tmp.replace(/0/g,"").length;

    let num2 = 0;
    
    while( num2 !== num ){
        n++;
        num2 = n.toString(2).replace(/0/g,"").length;
        answer = n.toString();
    }
    
     return Number(answer);
    
}