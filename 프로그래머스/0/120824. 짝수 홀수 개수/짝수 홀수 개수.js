function solution(num_list) {
    var answer = [];
    
    let even = 0;
    let odd = 0
    for( i = 0; i < num_list.length; i++){
        num_list[i] % 2 == 0 ? even++ : odd++;
    }
    return answer = [even, odd];
    
}