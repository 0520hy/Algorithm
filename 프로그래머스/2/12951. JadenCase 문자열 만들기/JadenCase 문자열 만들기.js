function solution(s) {
   
   
   let tmp = s.toLowerCase();
    
   return tmp.replace(/\b[a-z]/g, first => first.toUpperCase())
    // \b 문자의 시작 부분 찾기
    // g 전역 검색
    
}
