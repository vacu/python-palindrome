import re

try:
    import palindrome as p

    text = '''Python coding exercise: Palindrome filter.
    A palindrome is a word that reads the same backwards as forwards (e.g.
    "detartrated".) Write a script to read any plain text document from stdin. For
    example, use the content of this file as a testset. Filter for just the
    palindromes that are longer than 1 character. Output them, one per line, to
    stdout. Preserve the order of first occurrence, but only output each palindrome
    once.

    Consider whether your code runs fast like a racecar on large inputs, e.g.
    larger than RAM. Under what circumstances might it have to deal with an
    infinitely large input stream?

    We have a tenet that all non-throwaway code should be well tested, developed
    using TDD, and should generally raise on unresolvable errors or ambiguities.

    Don't forget to let us know what version of Python you're using, and generally
    present your solution so that we can install any dependencies, see your tests
    pass, and run your code, with minimum of fuss.
    '''

    palindrome  = p.Palindrome()
    words       = palindrome.splitText(text)

    for word in words:
        if palindrome.isPalindrome(word):
            print(word)

    print('======================================')

    palindromes = []
    try:
        with open('text.txt') as f:
            content = f.readlines()

            for line in content:
                words = palindrome.splitText(text)

                for word in words:
                    if palindrome.isPalindrome(word):
                        if word not in palindromes:
                            palindromes.append(word)
    except IOError:
        print('Could not open the file!')

    for p in palindromes:
        print(p)
except ImportError:
    print('Couldn\'t import palindrome')
