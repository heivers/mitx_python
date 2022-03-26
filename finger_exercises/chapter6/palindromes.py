import string

def is_palindrome(s):
    """Assumes s is a str
    Return True if letters in s form a palindrome.
    False otherwise. Non-letters and capitalization are ignored"""

    def to_chars(s):
        s = s.lower()
        letters = ""
        for c in s:
            if c in string.ascii_lowercase:
                letters += c
        return letters
    
    def is_pal(s):
        print(" is_pal called with", s)
        if len(s) <=1:
            print(" about to return True from base_case")
            return True
        else:
            answer = s[0] == s[-1] and is_pal(s[1:-1])
            print(" About to return", answer, "for", s)
            return answer
    
    return is_pal(to_chars(s))

print(is_palindrome("lol"))
print(is_palindrome("asap"))
print(is_palindrome("DogGod"))