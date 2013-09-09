from collections import Counter
import math

D = 1.0 
starter = '<s>'
ender = '</s>'

class CustomLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.bigrams = []
    self.bifreqs = []
    self.unigrams= []
    self.unifreq = []
    self.followers = dict() 
    self.preceders = dict()
    self.train(corpus)
    

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    for sentence in corpus.corpus: # iterate over sentences in the corpus
        lastword = ""
        for datum in sentence.data: # iterate over datums in the sentence
            word = datum.word # get the word
            if lastword:
                self.bigrams.append(lastword + " " + word) 
                if lastword in self.followers:
                    self.followers[lastword].add(word)
                else:
                    self.followers[lastword] = set()
                    self.followers[lastword].add(word)
                if word in self.preceders:
                    self.preceders[word].add(lastword)
                else:
                    self.preceders[word] = set()
                    self.preceders[word].add(lastword)
            self.unigrams.append(word)
            lastword = word
    self.bifreqs = Counter(self.bigrams)
    self.unifreq = Counter(self.unigrams)


  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0.0
    lastword = ""
    N = len(self.unifreq)
    #print sentence
    for token in sentence:
        count = self.unifreq[lastword]
        if count == 0:
            lastword = token
            continue
        pair = lastword + " " + token
        V = self.bifreqs[pair] * 1.0
        p1 = (V  - D) / count 
        if p1 < 0 : p1 = 0
        lmda = (D / count) * len(self.followers[lastword]) 
        if token in self.preceders:
            p2 = len(self.preceders[token]) * 1.0 / len(self.bigrams)
        else:
            p2 = .00000000000001 
        score += math.log(p1 + lmda * p2)
        #print V, p1, lmda, p2
        lastword = token
    return score
