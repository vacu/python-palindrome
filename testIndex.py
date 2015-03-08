import unittest
import palindrome as p

class TestIndexFunctions(unittest.TestCase):
    def setUp(self):
        self.text = '''Python coding exercise: Palindrome filter.
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

        self.wordPalindrome     = 'detartrated'
        self.wordNotPalindrome  = 'ambiguities'
        self.wordOneLetter      = 'a'

        self.palindrome = p.Palindrome()

    def test_splitText(self):
        words = self.palindrome.splitText(self.text)

        self.assertNotIsInstance(words, basestring)

    def test_isPalindrome(self):
        check = self.palindrome.isPalindrome(self.wordPalindrome)
        self.assertTrue(check)

    def test_notPalindrome(self):
        check = self.palindrome.isPalindrome(self.wordNotPalindrome)
        self.assertFalse(check)

    def test_oneLetterPalindrome(self):
        check = self.palindrome.isPalindrome(self.wordOneLetter)
        self.assertFalse(check)

if __name__ == '__main__':
    unittest.main()
