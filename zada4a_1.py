'''
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of
the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is
prime return the string '(integer) is prime
'''

def divisors(integer):
    list = []
    for i in range(2, integer):
        if integer % i == 0:
            list.append(i)
    return list if list else str(integer) + ' is prime'
print(divisors(12))