function solution(n) {
    var primes = [];
    var isPrime = new Array(n + 1).fill(true);

    for (var i = 2; i <= n; i++) {
        if (isPrime[i]) {
            primes.push(i); // 소수를 배열에 추가
            for (var j = i * i; j <= n; j += i) {
                isPrime[j] = false; // 소수의 배수들을 제거
            }
        }
    }

    return primes.length;
}


