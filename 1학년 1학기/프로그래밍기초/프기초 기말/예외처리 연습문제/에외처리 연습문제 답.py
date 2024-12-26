


def vowel_numbering(word):
    number = 1
    newword = ""
    for c in word:
        if c in ['a', 'e', 'i', 'o', 'u']:
            newword += str(number)
            number += 1
        else:
            newword += c
    return newword

# 테스트
print(vowel_numbering("apple"))  # 출력: "1p2pl3"
print(vowel_numbering("banana")) # 출력: "b1n2n3"
