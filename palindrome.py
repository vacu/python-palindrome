import re

class Palindrome:
    def __init__(self):
        self.data = []

    def splitText(self, text):
        return re.findall(r'\w+[-]\w+|\w+', text)

    def isPalindrome(self, word):
        if word == word[::-1] and len(word) > 1:
            return True
