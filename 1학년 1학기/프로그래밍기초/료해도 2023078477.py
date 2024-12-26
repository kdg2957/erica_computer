

import random

# 사용자로부터 단어를 입력 받아 거울에 비춰서 뒤집은 결과를 출력하는 함수
def reverse_word():
    word = input("단어를 입력하세요: ")
    reversed_word = word[::-1]  # 단어를 거꾸로 뒤집는다.
    print(word, "을(를) 거울에 비추면", reversed_word, "이(가) 됩니다.")

# 파일에서 단어를 읽어와서 정렬하여 리스트로 반환하는 함수
def load_words(file):
    with open(file, "r", encoding="UTF-8") as f:
        words = [line.strip() for line in f.readlines()]  # 각 줄의 공백 제거 후 리스트에 추가
    words.sort()  # 단어를 알파벳 순으로 정렬
    return words

# 단어 리스트에서 무작위로 하나의 단어를 선택하여 반환하는 함수
def pick_a_word(words):
    n = len(words)
    index = random.randrange(n)
    return words[index]

# 단어에서 일부 문자를 숨기고 숨김 결과와 숨겨진 문자를 반환하는 함수
def puncture_word(word, n):
    target = random.sample(word, n)  # 단어에서 n개의 문자를 무작위로 선택하여 리스트로 반환
    result = ""
    for s in word:
        if s in target:
            result = result + "_"
        else:
            result = result + s
    return result, target

# 사용자가 추측한 문자를 검사하고 결과를 반환하는 함수
def guess(word, quiz, target):
    while True:
        c = input('알파벳을 추측하세요 (a-z): ')
        if len(c) != 1 or not c.isalpha() or c < 'a' or c > 'z':
            print("올바른 형식의 알파벳을 입력하세요.")
        else:
            break

    while c in target:
        target.remove(c)

    quiz = ""
    for s in word:
        if s in target:
            quiz = quiz + "_"
        else:
            quiz = quiz + s
    return quiz, target

# 메인 함수: 게임의 전체 흐름을 관리
def main():
    print("단어 맞추기 게임에 오신 것을 환영합니다!")
    sorted_words = load_words("words_sample.txt")
    picked_word = pick_a_word(sorted_words)
    print("맞추어야 할 단어를 선택했습니다.")
    difficulty = int(input("난이도를 선택하세요 (1: 초급, 2: 중급, 3: 고급): "))

    if difficulty == 1:
        n = len(picked_word) // 3
    elif difficulty == 2:
        n = len(picked_word) // 2
    else:
        n = len(picked_word)

    quiz_word, target = puncture_word(picked_word, n)

    count = 5
    while target != []:
        print(quiz_word)
        print(target)
        quiz_word, target = guess(picked_word, quiz_word, target)
        count -= 1
        if count == 0:
            print("정답을 맞히지 못했습니다. 정답은:", picked_word)
            break

    if '_' not in quiz_word:
        print("축하합니다! 정답을 맞혔습니다.")

# 메인 함수 호출
main()


