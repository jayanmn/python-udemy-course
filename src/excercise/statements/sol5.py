# 5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
#    #Code in this cell

for num in range(1, 101):
    out = ""
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz for {}".format(num))
    elif num % 5 == 0:
        print("Buzz for {}".format(num))
    elif num % 3 == 0:
        print("Fizz for {}".format(num))
