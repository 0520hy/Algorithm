function solution(n, lost, reserve) {
    
    
    let answer = 0;
    let l = lost.filter((e) => !reserve.includes(e)).sort((a,b)=>a-b);
    let r = reserve.filter((e) => !lost.includes(e)).sort((a,b)=>a-b);
    
    for ( let i = 0; i<l.length; i++){
        for( let j = 0; j<r.length; j++){
            if(l[i]-1 == r[j] ||l[i]+1 == r[j] ){
               l.shift(); 
                     
        }
        }}
     return n - l.length;
    
    
    
}