from collections import Counter
import math

class StupidBackoffLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.bigrams = []
    self.bifreqs = []
    self.firstwords = []
    self.firstfreq = []
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    for sentence in corpus.corpus: # iterate over sentences in the corpus
        lastword = ""
        for datum in sentence.data: # iterate over datums in the sentence
            word = datum.word # get the word
            if lastword:
                self.bigrams.append(lastword + " " + word) 
            self.firstwords.append(word)
            lastword = word
    self.bifreqs = Counter(self.bigrams)
    self.firstfreq = Counter(self.firstwords)

  
  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0.0
    lastword = ""
    N = len(self.firstwords)
    V = len(self.firstfreq)
    p = 0.4 / (N + V)
    for token in sentence:
        count = self.firstfreq[lastword]
        pair = lastword + " " + token
        V = self.bifreqs[pair] * 1.0
        #print V, count, len(self.firstfreq)
        if V:
            score += math.log( V / count)
        else:
            score += math.log( (self.firstfreq[token] + 1) * p)
        lastword = token
    return score 
