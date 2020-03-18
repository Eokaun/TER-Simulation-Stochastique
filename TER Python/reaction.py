import random

class Reaction:
    reactifs = [('Es', 'E'), ('S', 'P')]
    results = ['S', 'Es']
    prob = [0.5, 0.07]

    def __init__(self, list_reactif, list_result, list_p):
        self.reactifs.extend(list_reactif)
        self.results.extend(list_result)
        self.prob=list_p

    def reaction(self, pair_react):
        ind = self.reactifs.index(pair_react)
        if random.random() <= self.prob[ind]:
            return self.results[ind]
        else:
            return self.reactifs[ind]

