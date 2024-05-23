#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

# Call the function to start the countdown
happy_new_year()

def square_integers(int_list):
    squared_list = [x ** 2 for x in int_list]
    return squared_list


result1 = square_integers([1, 2, 3, 4, 5])
result2 = square_integers([-1, -2, -3, -4, -5])

print(result1)
print(result2)  



def fizzbuzz():
    i = 1
    while i <=100:
        if i % 3==0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0 :
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
        i+=1
fizzbuzz()        
        