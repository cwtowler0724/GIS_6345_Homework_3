word = input('Enter your word:    ')

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <=2 and word[0] == word[-1]:
        return True
    elif word[0] != word[-1]:
       return False
    return is_palindrome(middle(word))

print(is_palindrome(word))
