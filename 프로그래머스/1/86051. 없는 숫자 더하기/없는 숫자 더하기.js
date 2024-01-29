function solution(numbers) {

    var arr = [0,1,2,3,4,5,6,7,8,9];
    var sum = 0;
    
    var diff = arr.filter(x => !numbers.includes(x));
    
     diff.forEach( num => {sum += num});
    
      return sum;
}