from checker import *

###############################################################################
#
# 2023년
# 프로그래밍기초 Programming Fundamentals
# 기말고사 뼈대코드 Finalterm. Skeleton Code
#
###############################################################################
#
# 학번(student id) :2021092060
# 이름(name) :문서찬
#
###############################################################################
# 1.1
###############################################################################


def median(x, y):
    add = x + y
    if add % 2 == 0:
        return int(add / 2)
    else:
        return -1

# median(21, 19)
# median(23, 22)
# run_case1_1("1.1", median)

###############################################################################
# 1.2
###############################################################################


def is_balanced(x, y):
    if type(x) != int or type(y) != int:
        return False
    if not ((10 <= x <= 99) and (10 <= y <= 99)):
        return False
    return (median(x, y) != -1) and (median(x, y)) % 10 == 0

# is_balanced(21, 19)
# is_balanced(21, 18)
# run_case1_2("1.2", is_balanced)

###############################################################################
# 1.3
###############################################################################


def solve(x, y):
    if is_balanced(x, y):
        print(f"{x} x {y}")
        avg = median(x, y)
        if x <= y:
            num = avg - x
            print(f"= ( {avg} - {num} ) x ( {avg} + {num} )")
        else:
            num = avg - y
            print(f"= ( {avg} + {num} ) x ( {avg} - {num} )")
        print(f"= {avg} x {avg} - {num} x {num}")
        print(f"= {avg * avg} - {num * num}")
        print(f"= {(avg * avg) - (num * num)}")

    else:
        print(f"{x} x {y} = ?")

# solve(21, 19)
# solve(18, 22)
# run_case1_1("1.1", is_balanced)
# run_case1_3("1.3", solve)

###############################################################################
# 2.1
###############################################################################


def lowercase(s):
    ans = ""
    for c in s:
        if 64 < ord(c) < 91:
            ans += chr(ord(c) + 32)
        else:
            ans += c
    return ans


# print(lowercase("McDonald"))
# run_case2_1("2.1", lowercase)

###############################################################################
# 2.2
###############################################################################


def split_words(s):
    rs = []
    s = lowercase(s)
    temp = ""
    for c in s:
        if 96 < ord(c) < 123:
            temp += c
        else:
            if len(temp) >= 2:
                rs.append(temp)
                temp = ""
            else:
                temp = ""
    return rs

# print(split_words("It's High Noon..."))
# run_case2_2("2.2", split_words)

###############################################################################
# 2.3
###############################################################################


def word_counter(file):
    f = open(file, "r", encoding="UTF-8")
    words = {}
    text = f.read()
    ls = split_words(text)
    for i in ls:
        cnt = 0
        while i in ls:
            ls.remove(i)
            cnt += 1
        words[i] = cnt
    return words


# print(word_counter("sample2.txt"))
# run_case2_3("2.3", word_counter)

###############################################################################
# 2.4
###############################################################################


def most_used_words(file, n):
    words = word_counter(file)
    # ...
    return None


def print_words(ws):
    for w, frequency in ws:
        print(w, ":", frequency)


booktitle = "prideandprejudice.txt"
# print(most_used_words(booktitle, 5))
# print_words(most_used_words(booktitle, 5))
# run_case2_4("2.4", most_used_words)

###############################################################################


def run_all():
    run_case1_1("1.1", median)
    run_case1_2("1.2", is_balanced)
    run_case1_3("1.3", solve)
    run_case2_1("2.1", lowercase)
    run_case2_2("2.2", split_words)
    run_case2_3("2.3", word_counter)
    run_case2_4("2.4", most_used_words)


# run_all()
