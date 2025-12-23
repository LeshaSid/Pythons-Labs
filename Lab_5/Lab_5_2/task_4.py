def are_anagrams(str1, str2):
    str1 = str(str1).lower().replace(" ", "")
    str2 = str(str2).lower().replace(" ", "")
    if len(str1) != len(str2):
        return False
    else:
        sorted1 = sorted(str1)
        sorted2 = sorted(str2)
        
        for i in range(len(sorted1)):
            if sorted1[i] != sorted2[i]:
                return False
                break
    return True

def test_are_anagrams_basic():
    assert are_anagrams("пила", "липа") is True

def test_are_anagrams_different_case():
    assert are_anagrams("Работа", "Отраба") is True

def test_are_anagrams_with_spaces():
    assert are_anagrams("апельсин", "спаниель") is True

def test_are_anagrams_false():
    assert are_anagrams("слово", "плово") is False

def test_are_anagrams_numbers():
    assert are_anagrams(123, 321) is True

def test_are_anagrams_empty():
    assert are_anagrams("", "") is True