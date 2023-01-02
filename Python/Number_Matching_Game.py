import random

# 랜덤모듈을 사용하여 1~100 까지 수 중, 랜덤 수 뽑기 (정답)
n = random.randrange(1,101)

# 게임 가능 기회 (총 10회)
opp = 1

# 알맞지 않은 수, 문자를 입력하였을 때 출력
flag = "게임 하기 싫으세요😡?"

# 10번의 기회가 넘지 않았을 때 실행 (while 문이 True)
while opp <= 10:
    num = (input("1에서 100까지 수를 입력하세요 : "))    # 사용자가 수를 입력
    
    # 입력한 값이 숫자인지 확인
    if num.isdigit() == True:
    # isdigit() : 문자열이 수로 이루어졌는 지 확인하는 명령어

        # 입력받은 수가 1~100 사이의 수이면 게임 실행
        if (int(num) > 0) and (int(num) <= 100):

            # 정답일 경우 게임 종료
            if int(num) == n:  
                print("정답은", n, "입니다")
                print("축하합니다😎. 프로그램을 종료합니다.")
                break

            # 정답보다 수가 작을 경우
            elif int(num) < n: 
                print("땡🤣!! 더 큰 수를 입력하세요")
                print("남은 입력 횟수 : ", (10 - opp))  # 게임을 할 수 있는 기회가 줄어들었다는 것을 보여줌
                opp += 1    # opp의 값을 1씩 증가 시켜서 기회가 줄어들도록 설정
                # 게임을 다시 진행
                # 숫자를 재입력받기 위해 while문 처음으로 이동
                continue

            # 정답보다 수가 클 경우 (작을 경우와 동일하게 진행)
            elif int(num) > n:
                
                print("땡🤣!! 더 작은 수를 입력하세요")
                print("남은 입력 횟수 : ", (10 - opp))
                opp += 1
                continue


        # 입력받은 값이 0보다 작거나 100보다 클 경우
        elif (int(num) > 100) or (int(num) < 0):

            # 알맞은 입력이 아님을 알려줌 ( flag = "게임 하기 싫으세요😡?" )
            print(flag)
            break   # 게임 종료

    # 입력받은 값이 수가 아닐 경우
    else:
        print(flag)
        break # 게임 종료

# 입력 기회가 끝났을 경우
if opp > 10:
    print("아쉽군요😂 입력기회가 10번 지났습니다!😜")