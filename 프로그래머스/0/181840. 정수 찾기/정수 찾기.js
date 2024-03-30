function solution(num_list, n) {
    let answer = num_list.find((el) => el == n)
    return  answer > 0 ? 1 : 0;
}