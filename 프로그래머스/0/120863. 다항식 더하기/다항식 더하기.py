def solution(polynomial):
    terms = polynomial.split()
    
    x_coeff = 0
    constant = 0

    for term in terms:
        if term == "+":
            continue
        
        if "x" in term:
            if term == "x":
                x_coeff += 1
            else:
                x_coeff += int(term.replace('x', ''))
        else:
            constant += int(term)
    

    result_parts = []
    if x_coeff != 0:
        if x_coeff == 1:
            result_parts.append("x")
        else:
            result_parts.append(f"{x_coeff}x")
    if constant != 0:
        result_parts.append(str(constant))
    
    return " + ".join(result_parts)