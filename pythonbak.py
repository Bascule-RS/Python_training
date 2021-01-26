#BEST SOLUTIONS:
def words_order(text: str, words: list) -> bool:

    return words == [word for word in text.split() if word in words and words.count(word) < 2]



if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
 ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
 ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
 ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
 ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def words_order(text, words):
    text_words = {w for w in text.split() if w in words}
    return list(sorted(text_words, key=text.index)) == words
    
def words_order(text: str, words: list) -> bool:
  return list(dict.fromkeys([word for word in text.split() if word in words])) == words
  

if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    
#ma solution:

import math;
def checkio(number: int) -> int:
    return math.prod([int(x) for x in str(number) if int(x) != 0])
    
    
    
####is all upper:
#my code:
    
def is_all_upper(text: str) -> bool:
    return True if text.isupper() else False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
#other solutions :

def is_all_upper(text: str) -> bool:
    # your code here
    return text.isupper()
    
def is_all_upper(text: str) -> bool:
    # your code here
    text = ''.join([i for i in text if i.isalpha()])
    if not text:
        return False
    return text == text.upper()
    


def is_all_upper(text: str) -> bool:
    # your code here
    if not any(c.isalpha() for c in text):
      return False
    return text == text.upper()