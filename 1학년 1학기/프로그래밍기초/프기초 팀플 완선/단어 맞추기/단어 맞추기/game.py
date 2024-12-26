import random

class GameManager():
    def __init__(self, attempt_count:int):
        self.words = []
        self.difficulty = 1
        self.max_attempt = attempt_count
        self.attempt_count = attempt_count

        self.answer = ''
        self.quiz = ''
        self.targets = []

        self.used_alphabets = []


    def load_words(self, file):
        with open(file, 'r', encoding="UTF-8") as f:
            for word in f.readlines():
                self.words.append(word.strip('\n'))


    def puncture_word(self) -> str:
        quiz = ''

        for s in self.answer:
            quiz += '_' if s in self.targets else s
        
        self.quiz = quiz


    def puncture_random(self):
        word = self.answer
        
        if self.difficulty == 0:
            n = len(set(word))// 3
        elif self.difficulty == 1:
            n = len(set(word)) // 2
        else:
            n = len(set(word))

        self.targets = random.sample(list(set(word)), n)
        self.puncture_word()

        self.used_alphabets = []
        for alphabet in set(self.answer):
            if alphabet in self.targets:
                continue

            self.used_alphabets.append(alphabet)
    

    def get_new_quiz(self):
        while True:
            try:
                self.answer = random.sample(self.words, 1)[0]
                assert 3 <= len(self.answer) <= 15
            except AssertionError:
                continue
            else:
                break
            
        self.puncture_random()


    def guess_letter(self, alphabet):
        self.used_alphabets.append(alphabet)

        if alphabet not in self.targets:
            self.attempt_count -= 1
            return False
        
        self.targets.remove(alphabet)
        self.puncture_word()
        return True
    

    def guess_word(self, word):
        if word != self.answer:
            self.attempt_count -= 1
            return False
        
        self.targets = []
        return True