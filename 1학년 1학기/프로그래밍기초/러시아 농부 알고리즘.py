def multify(m, n, algorythm=""):
    # 1. 재귀함수
    if algorythm == "":
        if n > 1:
            if n % 2 == 0:
                return multify(m * 2, n // 2)
            else:
                return m + multify(m * 2, n // 2)
        else:
            return m
    
    # 2. 꼬리재귀함수
    if algorythm == "tail":
        def loop(m, n, result):
            if n > 1:
                if n % 2 == 0:
                    return loop(m * 2, n // 2, result)
                else:
                    return loop(m * 2, n // 2, result + m)
            else:
                return result + m

        return loop(m, n, 0)
    
    # 3. while문
    if algorythm == "while":
        result = 0

        while n > 1:
            if n % 2 != 0:
                result += m
            m *= 2
            n //= 2
        return result + m
    

m, n = map(int, input().split())

# mult = multify(m, n)
# mult = multify(m, n, algorythm="tail")
mult = multify(m, n, algorythm="while")

print(f"{m} * {n} = {m * n}\nmultify({m}, {n}) = {mult}\nis program correct : {m * n == mult}")