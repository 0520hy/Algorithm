function solution(array, commands) {
   
 return commands.map(command => {
      const [i, j, k] = command;
      const answer = 
      array.slice(i-1,j)
            .sort(function(a, b) {return a - b});
    
      return answer[k-1];
  })
        
        }
   
