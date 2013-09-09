from collections import Counter
import math

class LaplaceUnigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    self.words = []
    self.freqs = []
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    for sentence in corpus.corpus: # iterate over sentences in the corpus
        for datum in sentence.data: # iterate over datums in the sentence
            word = datum.word # get the word
            self.words.append(word) 
    self.freqs = Counter(self.words)

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    score = 0.0
    N = len(self.words)
    V = len(self.freqs)
    p = 1.0 / (N + V)
    for token in sentence:
        score += math.log( (self.freqs[token] + 1) * p )
    return score 
