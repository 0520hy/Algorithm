function solution(array, n) {
    var answer = array.filter((el, idx) => el == n);
    return answer.length;
}