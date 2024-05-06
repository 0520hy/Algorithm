function solution(n, k) {
    
    let service = Math.floor(n / 10);
    console.log(service)
    return (n * 12000) + ((k-service) * 2000) ;
}