# 2023 중간 1번
if False:
    # 2023 중간 1.1번
    def log2r(num):
        if num > 1:
            return 1 + log2r(num // 2)
        else:
            return 0

    # 2023 중간 1.2번
    def log2r(num):
        def loop(num, result):
            if num > 1:
                return loop(num // 2, result + 1)
            else:
                return result
        
        return loop(num, 0)

    # 2023 중간 1.3번
    def log2r(num):
        result = 0

        while num > 1:
            num //= 2
            result += 1
        
        return result

# 2023 중간 2번
if False:
    # 2023 중간 2.1번
    def eval(you, com):
        win = ("P", "R", "S")
        lose = ("R", "S", "P")

        for i in range(3):
            if you == win[i] and com == lose[i]:
                return 1
            elif you == lose[i] and com == win[i]:
                return -1
        return 0
    
    # 2023 중간 2.2번
    def wins_r(game_logs):
        if len(game_logs) > 0:
            player, computer = game_logs[0][0], game_logs[0][1]

            if eval(player, computer) == 1:
                return 1 + wins_r(game_logs[1:])
            
            return wins_r(game_logs[1:])
        
        return 0
    
    # 2023 중간 2.3번
    def wins_t(game_logs):
        def loop(game_logs, result):
            player, computer = game_logs[0][0], game_logs[0][1]

            if len(game_logs) > 0:
                if eval(player, computer) == 1:
                    return loop(game_logs[1:], result + 1)
                
                return loop(game_logs[1:], result)
        
        return loop(game_logs, 0)
    
    # 2023 중간 2.4번
    def wins_w(game_logs):
        won_count = 0

        while len(game_logs) > 0:
            player, computer = game_logs[0][0], game_logs[0][1]

            if eval(player, computer) == 1:
                won_count += 1
            
            game_logs = game_logs[1:]
        
        return won_count
    
    # 2023 중간 2.5번
    def wins_f(game_logs):
        won_count = 0

        for log in game_logs:
            player, computer = log[0], log[1]

            if eval(player, computer) == 1:
                won_count += 1
        
        return won_count

# 2023 중간 3번
if False:
    # 2023 중간 3.1번
    def digit2morse(num):
        morse_num = ("-----", ".----", "..---", "...--", "....-", \
                     ".....", "-....", "--...", "---..", "----.")
        
        return morse_num[num]
    
    # 2023 중간 3.2번
    def is_digit_morse(input_morse):
        def is_morse_correct(morse):
            morse_num = ("-----", ".----", "..---", "...--", "....-", \
                        ".....", "-....", "--...", "---..", "----.")
            
            if morse in morse_num:
                return True
            return False


        test_morse = ""

        for signal in input_morse:
            if signal in (".", "-"):
                test_morse += signal
            elif signal == " ":
                if len(test_morse) == 0:
                    continue
                break
                
        return is_morse_correct(test_morse)
    
    # 2023 중간 3.3번
    def morse2digit(input_morse):
        def morse2digit(morse):
            morse_num = ("-----", ".----", "..---", "...--", "....-", \
                        ".....", "-....", "--...", "---..", "----.")
            
            if morse in morse_num:
                return morse_num.index(morse)
            return None


        test_morse = ""

        for signal in input_morse:
            if signal in (".", "-"):
                test_morse += signal
            elif signal == " ":
                if len(test_morse) == 0:
                    continue
                break
                
        return morse2digit(test_morse)
    
    # 2023 중간 3.4번
    def morse2number(input_morse):
        def morse2digit(morse):
            morse_num = ("-----", ".----", "..---", "...--", "....-", \
                        ".....", "-....", "--...", "---..", "----.")
            
            if morse in morse_num:
                return str(morse_num.index(morse))
            return -1


        result = ""
        test_morse = ""

        if len(input_morse) == 0:
            return -1

        for signal in input_morse:
            if signal in (".", "-"):
                test_morse += signal
            elif signal == " ":
                if len(test_morse) == 0:
                    continue
                
                if morse2digit(test_morse) == -1:
                    return -1

                result += morse2digit(test_morse)
                test_morse = ""

        if morse2digit(test_morse) == -1:
            return -1

        result += (morse2digit(test_morse))
                
        return result

# 2022 중간 5번
if False:
    # 2022 중간 5번 예시
    def check_number_with_comma(s:str):
        def loop(s:str):
            front, comma, rest = s.partition(",")

            if len(front) != 3:
                return False
            
            if comma == ",":
                return loop(rest)
            else:
                return False
            
        
        front, comma, rest = s.partition(",")

        if len(front) > 3:
            return False
        
        if int(front) == 0 or len(front) != len(str(int(front))):
            return False
        
        if comma == ",":
            return loop(rest)
        else:
            return True
        

    # 2022 중간 5번 풀이
    def check_number_with_comma(s:str):
        def loop(s:str):
            front, comma, rest = s.partition(",")
            return len(front) == 3 and (comma != "," or loop(rest))


        front, comma, rest = s.partition(",")
        return len(front) != 0 and \
            (len(front) < 4 and int(front) != 0 and len(front) == len(str(int(front))) and (comma != "," or loop(rest)))

        return len(front) == 3 and \
            int(front) >= 100 and (comma == "," and loop(rest) or comma != ",") or len(front) == 2 and \
            int(front) >= 10 and (comma == "," and loop(rest) or comma != ",") or len(front) == 1 and \
            int(front) != 0 and (comma == "," and loop(rest) or comma != ",")

    print(check_number_with_comma("")) # False

    print(check_number_with_comma("1")) # True

    print(check_number_with_comma("0")) # False

    print(check_number_with_comma("11")) # True

    print(check_number_with_comma("01")) # False

    print(check_number_with_comma("111")) # True

    print(check_number_with_comma("011")) # False
    print(check_number_with_comma("1111")) # False
    print(check_number_with_comma("0111")) # False

    print(check_number_with_comma("1,111")) # True
    print(check_number_with_comma("1,000,011")) # True
    print(check_number_with_comma("1,000,011,001")) # True

    print(check_number_with_comma("01,000,011,001")) # False
    print(check_number_with_comma("1,00,011,001")) # False
    print(check_number_with_comma("1,000,11,001")) # False
    print(check_number_with_comma("1,000,011,1")) # False