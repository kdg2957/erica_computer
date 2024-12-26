def reverse():
    x = input("단어를 입력하세요 : ")
    r = ""
    for c in x:
        r = c + r
    print("당신이 입력한", x, "를 거울에 비추면", r, "가 됩니다.")

def load_words(file):
    f = open(file, "r", encoding="UTF-8")
    words = []
    for word in f.readlines():
        words.append(word.strip('\n'))
    # 리스트 words 를 정렬한다.
    words.sort()
    return words

import random
def pick_a_word(words):
    n = len(words)
    index = random.randrange(n)
    return words[index]

def puncture_word(word, n):
    target = random.sample(word, n)
    result = ""
    for s in word:
        if s in target:
            result = result + "_"
        else:
            result = result + s
    return result, target

def guess(word, quiz, target):
    while True:
        c = input('guess a character (a-z) : ')
        if len(c) == 1 and c.islower():
            break
    
    # 수정 1.
    # c 의 길이가 1이고, a~z 사이의 영문소문자가 되도록 입력 검증을 추가
    if c in target:
        while c in target:        
            target.remove(c) # target 안에 c 가 여럿 있는 경우 처리
        # 수정 2.
        # 예: target = ['a', 'o', 'o'], c = 'o' 인 경우,
        # ['a', 'o'] 가 아니라 ['a'] 가 되어야 함
        quiz = ""
        for s in word:
            if s in target:
                quiz = quiz + "_"
            else:
                quiz = quiz + s
    return quiz, target


def main():
    sorted_words = load_words("words_sample.txt")
    picked_word = pick_a_word(sorted_words)
    # 확장 1.
    # n = 3 이 아니라 사용자가 입력한 난이도에 맞춰 조절하도록 수정
    m = len(picked_word)
    
    while True:
        s = input('Choose difficulty(1: Beginner, 2: Intermediate, 3: Advanced) : ')
        if not s.isdigit():
            continue
        difficulty = int(s)
    
        if difficulty == 1:
            n = m // 3
        elif difficulty == 2:
            n = m // 2
        elif difficulty == 3:
            n = m
        else:
            continue
        break
    
    quiz_word, target = puncture_word(picked_word, n)

    # 확장 2. 사용자가 입력한 문자 c 가 target에 없는 경우에
    # 횟수를 하나씩 소진하고,
    # 모두 소진하면 적절한 메시지와 함께 게임을 종료하도록 수정
    count = 5
    while target != [] and count > 0: # 반복 조건에 count 가 모두 소진된 경우를 반영
        print(quiz_word)
        print(target)
        target_len = len(target)
        quiz_word, target = guess(picked_word, quiz_word, target)
        if len(target) == target_len:
            count -= 1
        # count 를 감소

    # while 문을 빠져나왔을 때,
    # 정해진 횟수 안에 정답을 맞췄는지 여부에 따라 다른 메시지 출력
    if count > 0:    
        print("축하합니다!")
    else: 
        print("정답 맞히기 실패! 정답은", picked_word + "이었습니다!")

main()




