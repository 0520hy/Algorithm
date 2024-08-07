from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    
    while(people):
        escape = people.pop()
        
        if len(people) > 0 and escape + people[0] <= limit:
            people.popleft()
            
        answer += 1
    
    return answer