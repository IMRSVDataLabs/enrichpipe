from enrichpipe.ner import ner
import pytest
import spacy


def test_ner_inputs():
    """
    This function tests the expection handling of the ner function
    """
    nlp = spacy.load('en_core_web_sm')
    with pytest.raises(TypeError):
        ner(nlp, nlp)
    with pytest.raises(TypeError):
        ner(23, nlp)
    with pytest.raises(TypeError):
        ner([23], nlp)
    with pytest.raises(TypeError):
        ner(0.23, nlp)
    with pytest.raises(TypeError):
        ner(['hello'], nlp)


def test_ner():
    """
    This test creates toy data to test the ner function's behaviour
    """
    sentence = 'Tom and Sarah went shopping in Cuba while on Vacation'
    nlp = spacy.load('en_core_web_sm')
    entities = ner(sentence, nlp)

    # input test
    assert isinstance(sentence, str)

    # output check
    assert isinstance(entities, dict)
    for key in entities:
        assert isinstance(key, str)
    for i in entities.values():
        assert isinstance(i, list)
        for j in i:
            assert isinstance(j, str)
