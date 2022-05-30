import nltk
import pandas as pd 
import numpy as np
import yaml


def alphabet_check(sentence, lang):
    '''
    Checks if a particular text has characters in a suspected language
    
    Parameters
    ----------
    string : data of type str
             The sentence getting checked for containing the correct alphabet.
    lang : data of type str 
            The suspected language alphabet in which to check. must be defined above function.
    
    Return -> coupled tuple
    -------
    percentage : float
                percentage value of alphabet found that is NOT in the suspected language alphabet.
    not_lang : list 
                list of all characters NOT contained in the suspected language alphabet.
                
    Examples
    --------
    >>> from src.alphabet_check import alphabet_check
    >>> sentence = 'Hello World!'
    >>> lang = 'en'
    >>> alphabet_check(sentence, lang='en')
    >>> (0.0, [])
    >>> alphabet_check(sentence, lang='uk')
    >>> (0.0, ['h', 'e', 'l', 'o', 'w', 'r', 'd'])
    >>> alphabet_check(sentence, lang='uk) #sentence contains some non-Eukraine letters
    >>> (0.03, ['s', 'h', 'e', 'i', 'n', 'v', 'r', 't', 'd', 'o', 'p', 'a']) 
    >>> alphabet_check(sentence, lang='ar')
    >>> 'Language Not Found'
    '''

    languages = {
        'uk' : 'їґяшертиуіопющєасдфгчйкльжзхцвбнм ЇҐЯШЕРТИУІОПЮЩЄАСДФГЧЙКЛЬЖЗХЦВБНМ 1234567890 ,!?."',
        'en' : 'qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM 1234567890 ,!?."',
        'ru': 'ёъяшертыуиопющэасдфгчйкльжзхцвбнм ЁЪЯШЕРТЫУИОПЮЩЭАСДФГЧЙКЛЬЖЗХЦВБНМ 1234567890 ,!?."'
    }

    if not isinstance(sentence, str):
            raise TypeError(
                "Input text needs to be of type string"
                )

    if not isinstance(lang, str):
            raise TypeError(
                "Input language needs to be of type string"
                )

    if lang not in languages:
            raise TypeError(
                "Please ensure the list of languages contains the specified language"
            )

    letters = languages.get(lang)
    not_lang = []
    total = len(sentence)

    try: 
        for character in sentence:
            num_not_lang = 0
            if character in letters:
                continue
            if character not in letters:
                not_lang.append(character)
                num_not_lang += 1
        for i in range(len(not_lang)):
            not_lang[i] = not_lang[i].lower()
        not_lang = list(dict.fromkeys(not_lang))
        percentage = round(num_not_lang/total, 2)
        return percentage, not_lang
    except:
        return 'Language Not Found'
