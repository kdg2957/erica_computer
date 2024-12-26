import os, random
os.getcwd()

def reverse():
    x = input("단어를 입력해주세요 :")
    r = ""
    for c in x:
        r = c+ r
    print("당신이 입력한", x, "를 거울에 비추면" , r , "가 됩니다.")
    
    
    
# words  = ["love", "poem", "fire", "wind"]
# 
# print(words)
# 
# words.append("water")
# 
# print(words)
# 
# words.remove("love")
# 
# print(words)

# for _ in range(10):
#     values = random.sample("abcd",3)
#     print(values)

def puncture_word(word, n):
    target = random.sample(word, n)
    result = ''
    for s in word:
        if s in target:
            result = result + "-"
            
        else:
            result = result + s
            
    return result, target




# f = open("words_sample.txt", "r", encoding="UTF-8")
# word = "good\n"
# casel = word[:len(word)]
# print(casel)
# 
# case2 = word[:len(word)-1]
# print(case2)
# 
# case3 = word.strㅑp('\n')
# 
# case4, _ = word.split(sep='\n')


def load_words(file):
    f = open(file, "r", encoding="UTF-8")

    words = []
    for word in f.readlines():
        words.append(word.strip("\n"))
        words.sort
    
    return words


def pick_a_word(words):
    n = len(words)
    index = random.randrange(n)
    
    return words[index]


def guess(solution, quiz, target):
    c = input("guess a char(a-z) : ")
    alpavet = ['a', 'b','c','d','e','f','g','h','i','j','k','l','o','p','q','r','s','t','u','v','w','x','y','z']
    if not(len(c) == 1 and c in alpavet):
        c = input("guess a char(a-z) : ")
    #입력 조건 확인하는 코드 추가하기( 길이가 1이고 a-z이어야 함)
    if c in target:
        
        for _ in range(n):
            target.remove(c)  #1회 이상 반복해야함
        
        for s in word:
            if s in target:
                quiz = quiz + "_"
                
            else:
                quiz = quiz + s
        return quiz, target
    else:
        return quiz, target
    
    
    
def main():
    sorted_words = load_words("words_sample.txt")
    picked_word = pick_a_word(sorted_words)
    quiz_word, target = puncture_word(picked_word, 3)
    print("당신을 위한 단어는", quiz_word, "입니다")