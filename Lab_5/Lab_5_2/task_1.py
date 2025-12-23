def count_words(s):
    s = s.lower()
    marks = '.,!?;:"()[]{}<>«»""' + "''" + '`~@#$%^&*_-+=|\\/'
    for m in marks:
        s = s.replace(m, ' ')
    ls = s.split()
    
    return len(ls)

def test_basic():
    assert count_words("Привет, мир!") == 2

def test_many_marks():
    assert count_words("Один... два-три!!! Четыре?") == 4

def test_empty():
    assert count_words("!!! @@@ ###") == 0