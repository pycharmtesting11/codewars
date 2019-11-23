def sum_two_smallest_numbers(numbers):
    # your code here
    numbers.sort()
    new_array = numbers[:2]
    return print(new_array[0] + new_array[1])
sum_two_smallest_numbers([1,10,7,3])