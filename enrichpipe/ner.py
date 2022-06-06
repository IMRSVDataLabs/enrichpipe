import spacy
import os
path = os.path.abspath('./spacy/en_core_web_sm/en_core_web_sm-3.3.0')
nlp = spacy.load(path)


def ner(sentence, nlp_tokenizer):
    """ The ner function finds the named entities or “real-world object” in a sentence string
    and returns a dictionary with the objects found, along with their label

    Parameters
    ----------
    sentence : data of type str
                Input sentence
    nlp_tokenizer: A spacy language Object of type spacy.lang
                A spacy tokenizer

    Return -> Dictionary of strings
    --------
    The named entity recognition objects found by spacy

    Examples
    --------
    >>> from enrichpipe.ner import ner
    >>> import spacy
    >>> nlp = spacy.load('en_core_web_sm')
    >>> sentence = 'Tom and Sarah went shopping in Cuba while on Vacation'
    >>> ner(sentence, nlp_tokenizer=nlp)
    >>> {'PERSON': ['Tom', 'Sarah'], 'GPE': ['Cuba']}
    >>> sentence='Hello World'
    >>> ner(sentence, nlp_tokenizer=nlp)
    >>> No Entities Found
    """
    if not isinstance(sentence, str):
        raise TypeError(
            "Input sentence must be of type string"
            )
    nlp_tokenizer = nlp
    doc = nlp_tokenizer(sentence)
    named_entities = {}
    for token in doc.ents:
        if token.label_ not in named_entities:
            named_entities[token.label_] = [token.text]
        elif token.label_ in named_entities:
            named_entities[token.label_].append(token.text)
    if any(named_entities):
        return named_entities
    else:
        print("No Entities Found")
