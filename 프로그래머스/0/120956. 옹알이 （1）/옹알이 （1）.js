function solution(babbling) {
    let answer = 0;
    for( let i = 0; i < babbling.length; i++){
        let word = babbling[i];
        word = word.replaceAll("aya"," ");
        word = word.replaceAll("ye"," ");
        word = word.replaceAll("woo"," ");
        word = word.replaceAll("ma"," ");
        word = word.replaceAll(" ","")
        if(word.length == 0) answer++;
    }
    return answer;
}