import datetime

def solution(a, b):
    day_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    answer = day_list[datetime.date(2016, a, b).weekday()]
    return answer