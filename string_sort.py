#a = 'ZENOVW'
#b = ''.join(sorted(a))
#print(b)

def longest(s1, s2):

    # Defining the Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Concatenating the Two Given Strings
    sum_string = s1 + s2

    # Declaring the Output Variable
    final_string = ''

    # Comparing whether a letter is in the string
    for x in alphabet:
        if x not in sum_string:
            continue
        if x in sum_string:
            final_string += x

    # returning the final output
    return final_string
print(longest('safdsa', 'asfdasfd'))