function solution(arr)
{
  let sol = [];
  for(i=0;i <arr.length;i++)
      if(arr[i] !== arr[i-1]){
          sol.push(arr[i]);
      }
    return sol;
}