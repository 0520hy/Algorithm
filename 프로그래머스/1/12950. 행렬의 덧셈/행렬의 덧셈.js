function solution(arr1, arr2) {
    
    
    return arr1.map((n, idx)=> n.map((m,idx2)=> m + arr2[idx][idx2]));
    
    
    }