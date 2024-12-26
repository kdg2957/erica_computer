

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
    while len(target) != 3:
        target = random.sample(word, n)
    result = ""
    for s in word:
        if s in target:
            result = result + "_"
        else:
            result = result + s
    return result, target

def guess(word, quiz, target):
    
    c = input('guess a character (a-z) : ')
    # 수정 1.
    # c 의 길이가 1이고, a~z 사이의 영문소문자가 되도록 입력 검증을 추가

    alpavet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    done = []
    while not(len(c) == 1 and c in alpavet and c in done):
        c = input('guess a character (a-z) retry: ')

    if c in target:
        while c in target:
            done.append(c)
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
    else:
        return quiz, target
    

def full_guess(word):
    full_word = input("전체 단어를 맞춰보시오")
    if full_word == word:
        print("정답이에용")
        
        return 1
    else:
        print("뭘 믿고 이걸 한 겨?")
        
        return 0




def main():
    sorted_words = load_words("words_sample.txt")
    picked_word = pick_a_word(sorted_words)
    # 확장 1.
    # n = 3 이 아니라 사용자가 입력한 난이도에 맞춰 조절하도록 수정
    n = int(input("난이도를 선택해주세요 1 2 3"))
    if n == 1:
        level = len(picked_word)// 3
        
    elif n == 2:
        level = len(picked_word) // 2
    
    else:
        level = len(picked_word)
    quiz_word, target = puncture_word(picked_word, level)

    # 확장 2. 사용자가 입력한 문자 c 가 target에 없는 경우에
    # 횟수를 하나씩 소진하고,
    # 모두 소진하면 적절한 메시지와 함께 게임을 종료하도록 수정
    count = 5
    answer = 0
    while target != [] and count != 0 and answer == 0: # 반복 조건에 count 가 모두 소진된 경우를 반영
        print(quiz_word)
        lenth = len(target)
        print(picked_word)
        print(target)
        
        selection = input("알파벳(1) or 단어(2)")
        while not (int(selection) == 1 or int(selection) == 2):
            selection = input("알파벳(1) or 단어(2) 1 또는 2를 선택해주세요")

            
        if int(selection) == 1:
        
            quiz_word, target = guess(picked_word, quiz_word, target)
            lenth_ch = len(target)
            if lenth == lenth_ch:
                count -= 1
        else:
            answer = full_guess(picked_word)
            if answer == 0:
                count -= 1
            


    # while 문을 빠져나왔을 때,
    # 정해진 횟수 안에 정답을 맞췄는지 여부에 따라 다른 메시지 출력
    if count != 0 : print(5-count, "번 틀리고 정답을 맞췄습니다")
    else: print("기회 5번을 다 소진하였습니다. ")
main()




