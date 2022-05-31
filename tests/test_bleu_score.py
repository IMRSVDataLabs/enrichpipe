from enrichpipe.bleu_score import bleu_score
import pytest


def test_bleu_score_inputs():
    """
    This function tests the expection handling of the bleu score function
    """
    hypothesis = 'Is there power at my home'
    ref1 = 'There is no power at my house'
    ref2 = 'There is no electricity at my house'
    refs = [ref1, ref2]
    weights = (0.5, 0.5)
    with pytest.raises(ValueError):
        bleu_score(refs, hypothesis, weights=(1, -0.2))
    with pytest.raises(TypeError):
        bleu_score(refs, hypothesis, weights=(5))
    with pytest.raises(TypeError):
        bleu_score(refs, hypothesis, weights=[0.5, 0.5])
    with pytest.raises(TypeError):
        bleu_score(refs, hypothesis, weights="hi")
    with pytest.raises(TypeError):
        bleu_score(ref1, hypothesis, weights)
    with pytest.raises(TypeError):
        bleu_score(2, hypothesis, weights)
    with pytest.raises(TypeError):
        bleu_score([2, 9, 8.5], hypothesis, weights)
    with pytest.raises(TypeError):
        bleu_score(ref1, [hypothesis], weights)
    with pytest.raises(TypeError):
        bleu_score(ref1, 5, weights)


def test_bleu_score():
    """
    This test creates toy data to test the bleu score function's behaviour.
    """
    hypothesis = 'Is there power at my home'
    reference1 = 'There is no power at my house'
    reference2 = 'There is no electricity at my house'
    refs = [reference1, reference2]
    weights = (0.5, 0.5)
    score = bleu_score(refs, hypothesis, weights)
    # input test
    assert isinstance(weights, tuple)
    assert isinstance(refs, list)
    assert isinstance(hypothesis, str)
    # output check
    assert isinstance(score, float)
