from random import choice

#задача https://codeforces.com/gym/102791/problem/A

n = int(input())

r = int(input())

y = int(input())

b = int(input())

list_numbers = [i for i in range(1,9)]

def func(list_numbers):
    
    while True:
        
        red = choice(list_numbers)
        yellow = choice(list_numbers)
        blue = choice(list_numbers)
        
        red_num = r * red
        yellow_num = y * yellow
        blue_num = b * blue
        
        result = red_num + yellow_num + blue_num
        
        if red - yellow > 1 or yellow - red > 1:
            pass
        
        elif red - blue > 1 or blue - red > 1:
            pass
        
        elif yellow - blue > 1 or blue - yellow > 1:
            pass
        
        elif result > n:
            pass
        
        else:
            return f'{red} red, {yellow} yellow, {blue} blue = {red + yellow +blue} toys'
            
        
print(func(list_numbers))

