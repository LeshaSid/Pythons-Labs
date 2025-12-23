def is_palindrome(s):
    s = str(s)
    if s == s[::-1]:
        return True
    else:
        return False


def test_is_palindrome_word():
    assert is_palindrome("лол") is True

def test_is_palindrome_not_word():
    assert is_palindrome("привет") is False

def test_is_palindrome_number():
    assert is_palindrome(12321) is True

def test_is_palindrome_not_number():
    assert is_palindrome(12345) is False

def test_is_palindrome_single_char():
    assert is_palindrome("а") is True

def test_is_palindrome_empty():
    assert is_palindrome("") is True

def test_is_palindrome_case():
    assert is_palindrome("Abba") is False