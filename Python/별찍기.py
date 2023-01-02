## 1. 공백이 앞에 있는 별찍기

# case 1 : 기본 반복문
for blank in range(5,-1,-1):
    star = 6 - blank
    print(" " * blank, "*" * star)

# case 2 : 중첩 반복문
for i in range(5):    
    for blank in range(5 - ( i + 1)):
        print(" ", end = "")

    for star in range(i + 1):
        print("*", end = "")    
    print()

## 2. 거꾸로 된 공백 삼각형 별찍기

# case 1 : 기본 반복문
for star in range(5,0,-1):
    blank = 5 - star
    print(' ' * blank, "*" * star)

# case 2 : 중첩 반복문
for i in range(5):    
    for blank in range( i + 1):
        print(" ", end = '')

    for star in range(5 - i):     # star = 5 - blank
        print("*", end = '')    
    print()

## 3. 정삼각형 별찍기

# case 1 : 기본 반복문
for i in range(4, -1, -1):
    print(' ' * i, '*' * (9 - (2 * i)))

# case 2 : 중첩 반복문
for i in range(5):    
    for balnk in range(5 - ( i + 1)):
        print(" " , end = '') 

    for star in range((2 * i) +1):
        print("*", end = '')     
    print()

## 4. 번외편 ! (별말고 하트 등 다른 문자 찍기)
for i in range(5):    

    for balnk in range(5 - (i+1)): 
        print(" "*2, end = "") 
        # * 이 아닌 다른 문자를 넣으면 공백 * 2 해주기( byte단위라서..)
        # 다른 문자보다 * 이 공백과 칸이 같아서 이쁨 !

    for star in range((2 * i) +1):
        print("♡", end = "") 
    print()