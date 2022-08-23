# 처음 시도한 코드
def solution(id_list, report, k):
    answer = ''
    id_dict = {x: 0 for x in id_list} # for return result
    report_dict = {x: 0 for x in id_list} # for report result

    report_list = []
    for i in report:
        report_list.append(tuple(i.split()))

    duplicate_list = set(report_list) # 중복을 제거한 신고 수
    for id in duplicate_list:
        report_dict[id[1]] += 1

    # 신고를 k 번 이상 당한 유저의 리스트 생성
    report_id = list({key: value for key, value in report_dict.items() if value >= k}.keys())

    for i in duplicate_list:
        if i[1] in report_id:
            id_dict[i[0]] += 1
    
    answer = list(id_dict.values())
        
    return answer

# 피드백을 본 후 코드
# 받아오는 리스트를 set으로 고쳐주면 더 간편하게 풀 수 있는 문제였음.
def solution(id_list, report, k):
    id_dict = {x: 0 for x in id_list} # for return result
    report_dict = {x: 0 for x in id_list} # for report result

    for id in set(report):
        report_dict[id.split()[1]] += 1

    report_id = list({key: value for key, value in report_dict.items() if value >= k}.keys())
    for id in set(report):
        if id.split()[1] in report_id:
            id_dict[id.split()[0]] += 1

    answer = list(id_dict.values())
    return answer
