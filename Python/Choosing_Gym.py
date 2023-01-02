# 각 헬스장의 정보를 담은 딕셔너리
health = {
            "학교 헬스장" : ["23", "bad"],
            "헬스장 A" : ["22", "best"],
            "헬스장 B" : ["18", "best"], 
            "헬스장 C" : ["20","good"],
            "헬스장 D": ["30", "good"]
}

# 딕셔너리 안의 item을 반복문으로 하나씩 돌기
for name in health:  

    # 각 헬스장의 비용
    cost = health[name][0]

    # 비용값에 따라 가중치를 설정
    # health 딕셔너리의 비용값을 비용의 가중치로 변경

    # 비용이 20만원보다 적을 경우
    if float(cost) <= 20:
        health[name][0] = 3    # 제일 높은 가중치 값 = 3
        # print("ch",health[name],cost)    # 확인코드

    # 비용이 20 ~ 23 만원 사이일 경우
    elif (float(cost) > 20) and (float(cost) < 23):
        health[name][0] = 2
        # print("ch",health[name],cost)   # 확인코드 

    # 비용이 23만원보다 비쌀 경우
    else:
        health[name][0] = 1

    # 각 헬스장의 거리
    distance = health[name][1]
    # health 딕셔너리의 거리값을 거리의 가중치로 변경

    if distance == "bad":
        health[name][1] = 1

    elif distance == "good":
        health[name][1] = 2

    # 거리가 가까울 경우 = best
    elif distance == "best":
        health[name][1] = 3    # 제일 높은 가중치 값 = 3

# 가중치의 합을 넣을 딕셔너리
values = {}

for name in health:
    value = health[name][0] + health[name][1]    # 비용가중치 + 거리가중치
    values[name] = value
    # print("name",name) 
    # print("values[name]:",values[name])  # 확인코드

# print("values : ", values)  # 확인코드

max_value = 0    # 제일 큰 가중치의 값을 넣을 변수


for i, value in values.items():
    # 가중치 합에서 제일 큰 가중치를 찾아 max_value로 설정
    if max_value < value:
        max_value = value

for name in health:
    # health 딕셔너리에서 가중치가 max_value인 헬스장 출력
    if values[name] == max_value: 
        print(name)

    # max_value가 아닐 경우 continue를 통해 반복문 처음으로 돌아감
    else:
        continue