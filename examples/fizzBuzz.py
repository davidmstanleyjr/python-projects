# Write a program in Python  that prints the numbers from 1 to 20.
# For multiples of 3 print "Fizz" instead of the number.
# For Multiples of 5 print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5 print "FizzBuzz".
# For number not divisible by 3, or 5, or both, print the number as is.

for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
