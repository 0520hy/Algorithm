function solution(sizes) {
    
    let answer = 0;
    let arr1 = [];
    let arr2 = [];
    
    for ( i= 0; i<sizes.length; i++){
        sizes[i].sort((a,b) => b-a);
        arr1.push(sizes[i][0]);
        arr2.push(sizes[i][1]);
    }
    
    const w = Math.max(...arr1);
    const h = Math.max(...arr2);
    
    return w * h;
    
}