# homework #01 2024052015 김동건
def average_score():
    print("Score Average Calculator")
    number = input("How many classes? ")
    while not number.isdigit():
        number = input("Enter positive number: ")
    number = int(number)
    total = 0
    count = 0
    while count < number:
        if count != number-1:
            left_score = '({} score left) : '.format(number-count)
        else:
            left_score = '(last score) : '
        prompt = "Enter your score: {}".format(left_score)
        score = input(prompt)
        while not score.isdigit():
            if count != number-1:
                prompt = '({} score left) : '.format(number-count)
            else:
                prompt = '(last score) : '
            score = input("Enter positive number {}".format(prompt))
        total = total + int(score)
        count = count + 1
    if number == 0:
        print("Your average score = 0.0")
    else:
        average = total / number
        print("Your average score =", round(average, 1))

average_score()