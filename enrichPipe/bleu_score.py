import nltk
import pandas as pd 
import numpy as np

def bleu_score(references, hypothesis, weights = (0.5, 0.5)):
    '''     
    The BLEU metric scores a translation on a scale of 0 to 1, 
    in an attempt to measure the adequacy and fluency of the Machine Learning output
    
    Parameters
    ----------
    references : list of data of type str
                 Reference sentences
    hypothesis: data of type str
                A hypothesis sentence; often is a machine translated text
    
    Return -> List of floats
    --------
    The sentence-level BLEU score. Returns a list if multiple weights were supplied.
    
    Examples
    --------

    Refer to nltk docs
    
    '''
    if not isinstance(weights, tuple):
        raise TypeError(
            "Input weights must be passed in as a tuple of floats"
            )
    for w in weights:
        if w < 0.0 or w > 1.0:
            raise ValueError(
                "weights must be a float between 0.0 and 1.0"
            )
    for w in weights:
        if not isinstance(w, float):
            raise TypeError(
                "weights must be of type float"
            )
    if not isinstance(references, list):
        raise TypeError(
            "References is expecting a variable of type list" #comma separated text data
                       )
    for ref in references:
        if not isinstance(ref, str):
            raise TypeError(
            "Each reference needs to be of type str+")
    if not isinstance(hypothesis, str):
        raise TypeError(
            "Hypothesis is expecting a variable of type string" #single sentence
                        )
    if len(weights) < 2:
        raise ValueError(
            "weights must contain at least 2 float values"
        )
        
    list_of_references = []
    for ref in references:
        ref_split = ref.split()
        list_of_references.append(ref_split)
    hyp_split = hypothesis.split()
    BLEU_result = nltk.translate.bleu_score.sentence_bleu(list_of_references, hyp_split,  weights = weights)
    return BLEU_result