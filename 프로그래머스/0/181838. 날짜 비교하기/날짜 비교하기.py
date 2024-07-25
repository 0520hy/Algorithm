from datetime import datetime

def solution(date1, date2):
    fir = datetime(date1[0], date1[1], date1[2])
    sec = datetime(date2[0], date2[1], date2[2])

    return 1 if fir < sec else 0