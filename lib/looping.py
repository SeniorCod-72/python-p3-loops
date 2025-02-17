#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")


    pass

def square_integers(int_list):
    # code goes here!
    return [x**2 for x in int_list]

    pass

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print ("FizzBuzz")
        elif num % 3 == 0:
            print ("Fizz")
        elif num % 5 == 0:
            print ("Buzz")
        else: 
            print(num)
        
    pass
# i = 0
# while i < 5:
#   print("Looping!")
#   i += 1