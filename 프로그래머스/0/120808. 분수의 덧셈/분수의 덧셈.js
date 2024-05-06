function solution(numer1, denom1, numer2, denom2) {

    
    let numer = numer1 * denom2 + numer2 * denom1;
    let denom = denom1 * denom2;
    
    const getGCD = (numer, denom) => ( numer % denom === 0 ? denom : getGCD(denom, numer % denom));
    
    const GCD = getGCD(numer,denom);
    
    return [numer/GCD,denom/GCD];
}