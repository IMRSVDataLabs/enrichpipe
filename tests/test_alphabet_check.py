import pytest
from enrichpipe.alphabet_check import alphabet_check


def test_alphabet_check():
    sentence = 'Hello World!'
    lang = 'uk'
    percent, not_lang = alphabet_check(sentence, lang)
    # input test
    assert isinstance(sentence, str)
    assert isinstance(lang, str)

    # output test
    assert isinstance(percent, float)
    assert isinstance(not_lang, list)


def test_alphabet_check_exceptions():
    languages = {
        'uk': 'їґяшертиуіопющєасдфгчйкльжзхцвбнм ЇҐЯШЕРТИУІОПЮЩЄАСДФГЧЙКЛЬЖЗХЦВБНМ 1234567890 ,!?."',
        'en': 'qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM 1234567890 ,!?."',
        'ru': 'ёъяшертыуиопющэасдфгчйкльжзхцвбнм ЁЪЯШЕРТЫУИОПЮЩЭАСДФГЧЙКЛЬЖЗХЦВБНМ 1234567890 ,!?."'
    }
    sentence = 'Hello World!'
    sentence2 = 'Happy Times!'
    with pytest.raises(TypeError):
        alphabet_check(23, lang='uk')
    with pytest.raises(TypeError):
        alphabet_check(0.8, lang='uk')
    with pytest.raises(TypeError):
        alphabet_check([sentence, sentence2], lang='uk')
    with pytest.raises(TypeError):
        alphabet_check(sentence, lang=languages)
    with pytest.raises(TypeError):
        alphabet_check(sentence, lang=0.8)
    with pytest.raises(TypeError):
        alphabet_check(sentence, lang=5)
