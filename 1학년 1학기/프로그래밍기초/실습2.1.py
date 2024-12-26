# from math import pi
# 
# r = float(input("radius : "))
# print("The area of a circle with radius", r , "is", round(pi*r**2,1))




# coin_500 = int(input(" 500 won? "))
# coin_100 = int(input(" 100 won? "))
# coin_50 = int(input(" 50 won? "))
# coin_10 = int(input(" 10 won? "))
# 
# total = coin_500*500 + coin_100*100 + coin_50*50 + coin_10*10
# 
# print("You have",total,"won in total")



# print("Fahrenheit to Celsius conversi")
# F = int(input("Degrees in Fahrenhei? "))
# C = (F-32)*5/9
# 
# print(round(C,1),"Degrees in Celsius")


# def coin_in_total(c500, c100, c50, c10):
#     return c500*500 + c100*100 + c50*50 + c10*10
#     
# print(coin_in_total(4,2,3,4))
# print(coin_in_total(9,2,3,4))
# print(coin_in_total(1,2,9,4))
# print(coin_in_total(4,5,3,4))
# print(coin_in_total(3,4,3,4))


# def fahrenheit2delsius(f):
#     return (f-32)*5/9
#     
# print(fahrenheit2delsius(67))
# print(round(fahrenheit2delsius(67),1))

import math
def complement_nine(n):
    k = len(str(n))
    return (10**k)-1-n
print(complement_nine(17))
    

    