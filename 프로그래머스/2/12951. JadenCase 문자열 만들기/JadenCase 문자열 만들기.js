function solution(s) {
   
   
   let tmp = s.toLowerCase();
    
   return tmp.replace(/\b[a-z]/g, letter => letter.toUpperCase())
    
}