function solution(price, money, count) {
    
    for(i = 1; i <= count; i++){
        money -= i*price;
    }
    if(money<0){
        return Math.abs(money);
    }else{
        return 0;
    }

    
}