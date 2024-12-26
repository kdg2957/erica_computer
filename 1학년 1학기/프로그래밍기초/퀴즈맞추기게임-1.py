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
        c = input('guess a character (a-z): ')
        if len(c) == 1 and c.islower():
            break
        else:
            print("소문자 알파벳로 다시 입력해주세요.")


    while c in target:
        target.remove(c)

    quiz = ""
    for s in word:
        if s in target:
            quiz += "_"
        else:
            quiz += s
    return quiz, target


def main():
    sorted_words = load_words("words_sample.txt")
    picked_word = pick_a_word(sorted_words)
    
    
    m = len(picked_word)
    difficulty = int(input("난이도를 정하세요  (1: 쉬움, 2: 중간, 3: 어려움): "))
    if difficulty == 1:
        n = m // 3
    elif difficulty == 2:
        n = m // 2
    elif difficulty == 3:
        n = m
    else:
        print("중간 난이도로 설정합니다")
        n = m // 2
        

    quiz_word, target = puncture_word(picked_word, n)

    count = 5  
    while count > 0 and target:
        print(quiz_word)
        print(target)
        quiz_word, target = guess(picked_word, quiz_word, target)
        count -= 1

    if target:
        print("게임이 종료되었습니다. 틀린 갯수는  '{}'.".format(picked_word))
    else:
        print("축하합니다! 당신이 추측한 단어는 '{}' 입니다! ".format(picked_word))

main()