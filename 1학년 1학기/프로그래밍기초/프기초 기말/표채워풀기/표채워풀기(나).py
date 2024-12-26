### 6.5 - 아이소그램 확인 (p.309)

def isisogram(word):
    while word != '' and word[1:] != '':
        if word[0] in word[1:]:
            return False
        else:
            word = word[1:]
    return True

### 6.6 - 아나그램 확인 (p.309-310)
# sort() 함수 사용 자제

# code : 6-24.py
def isanagram(word1,word2):
    while word1 != '':
        if word1[0] in word2:
            index = word2.find(word1[0])
            word1 = word1[1:]
            word2 = word2[:index] + word2[index+1:]
        else:
            return False
    return word2 == ''