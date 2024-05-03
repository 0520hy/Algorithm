function solution(array, height) {
    var answer = [];
    array.map((item) => {
       if( item > height ) answer.push(item)
    });
    return answer.length;
}