def solution(before, after):
    before = ''.join(sorted(before))
    after = ''.join(sorted(after))
    return 1 if before == after else 0