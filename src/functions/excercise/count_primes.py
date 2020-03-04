def count_primes(num):
    if num == 0 or num == 1:
        return 0

    prime_numbers = [2]
    for number in range(3, num, 2):  # Skip all even numbers by specifying step size of 2
        for y in prime_numbers:
            if number % y == 0:
                break  # it's not prime
        else:  # if for loop never break than number is primer
            prime_numbers.append(number)
        # if is_prime(number):
        #     prime_numbers.append(number)
    print(prime_numbers)
    return len(prime_numbers)
    pass
