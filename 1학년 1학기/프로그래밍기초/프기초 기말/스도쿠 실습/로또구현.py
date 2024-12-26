import random

def lotto645(num_rows):
    for _ in range(num_rows):
        numbers = []
        while len(numbers) < 6:
            num = random.randrange(1, 46)
            if num not in numbers:
                numbers.append(num)
        # 번호를 정렬
        numbers.sort()
        # 번호를 두 자리 형식으로 변환하여 문자열 리스트로 만듦
        formatted_numbers = [f"{num:02}" for num in numbers]
        # 번호를 공백으로 구분하여 출력
        
        
        for i in formatted_numbers:
            print(i, end= ' ')
        print()
        #print(" ".join(formatted_numbers))

# 예제 실행: 5개의 로또 번호 행 생성
lotto645(5)




def numbers_art(n):
    for i in range(n):
        for j in range(n):
            print(j+1, end=' ')
        print()

#numbers_art(5)
        
