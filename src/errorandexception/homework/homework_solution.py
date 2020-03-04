# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.
for i in ['a', 'b', 'c', 1, 2, 3, 4]:
    try:
        print(i ** 2)
    except:
        print("Not an integer.")

# Problem 2 Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to
# print 'All Done.'
x = 5
y = 0

try:
    z = x / y
except ZeroDivisionError:
    print("We have hit a math exception")
finally:
    print("All done.")


# Problem 3 Write a function that asks for an integer and prints the square of it. Use a while loop with a try,
# except, else block to account for incorrect inputs.
def ask():
    while True:  # Loop untill we have an integer
        try:
            num = int(input("Enter a number to get sqaure of it: "))
        except TypeError:
            print("Oops! You enter a non integer")
            print("Please try again!")
            continue
        else:
            break
    print("Square of number {} is {}".format(num, num ** 2))
    pass


ask()
