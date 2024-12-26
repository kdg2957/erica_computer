# def even(n):
#     return n % 2 == 0
# 
# print(even(13))
# print(even(26))
# 
# 

#x = int(input('Enter your number: '))
# if x % 2 == 0:
#     if x % 3 == 0:
#         print(x,'is divisible by 2 and 3')
#     else:
#         print(x,'is divisible by 2 but not by 3')
#         
# else:
#     if x % 3 == 0:
#         print(x, 'is divisible by 3 but not by 3')
#     else:
#         print(x, 'is not divisible by 2 or 3')


def smaller(x, y):
    if x < y:
        return x
    else:
        return y
# 
# 
# print(smaller(3,5))
# print(smaller(5,3))
# print(smaller(3,3))




# def smallest(x,y,z):
#     if x < y:
#         if x < z:
#             return x
#         else:
#             return z
#     else:
#         if y < z:
#             return y
#         else:
#             return z
# 
# print(smallest(3,5,9))
# print(smallest(5,3,9))
# print(smallest(5,9,3))
# print(smallest(3,9,5))
# print(smallest(9,3,5))
# print(smallest(9,5,3))
# print(smallest(3,3,5))
# print(smallest(5,3,3))
# print(smallest(3,5,3))
# print(smallest(3,3,3))

# def smallest(x,y,z):
#     return smaller(smaller(x,y),z)
# 
# print(smallest(3,5,9))
# print(smallest(5,3,9))
# print(smallest(5,9,3))
# print(smallest(3,9,5))
# print(smallest(9,3,5))
# print(smallest(9,5,3))
# print(smallest(3,3,5))
# print(smallest(5,3,3))
# print(smallest(3,5,3))
# print(smallest(3,3,3))

print('Score Average Calculator')
number = input("How many classes? ")

while not number.isdigit():
    number = input("Enter a positive number: ")
    
number = int(number)
total = 0
count = 0

while number > count:
    score = input("Enter your score: ")
    while not score.isdigit():
     score = input("Enter your score: (natural number only)")
    total += int(score)
    count += 1
    
    
if count > 0:
    print('Your average score =' , round(total/number,1))
else:
    print('Your average score = 0.0')
    
