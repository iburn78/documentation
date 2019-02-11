import math, sys
from konlpy.tag import Twitter

class BayesianFilterAK:
    def __init__(self):
        self.words = set()
        self.word_dict = {}
        self.cat_dict = {}

    def split(self, text):
        results = []
        twitter = Twitter()
        wordlist = twitter.pos(text, norm=True, stem=True)
        for word in wordlist:
            if word[1] not in ["Josa", "Eomi", "Punctuation"]:
                results.append(word[0])
        return results
    
    def inc_word(self, word, cat):
        if cat not in self.word_dict:
            self.word_dict[cat] = {}
        if word not in self.word_dict[cat]:
            self.word_dict[cat][word] = 1
        else:
            self.word_dict[cat][word] += 1
        self.words.add(word)
    
    def inc_cat(self, cat):
        if cat not in self.cat_dict:
            self.cat_dict[cat] = 1
        else:
            self.cat_dict[cat] += 1

    def fit(self, text, cat):
        splitted_words = self.split(text)
        for word in splitted_words: 
            self.inc_word(word, cat)
        self.inc_cat(cat)    
    
    def score(self, test_words, cat): 
        score = math.log(self.cat_prob(cat))
        for word in test_words: 
            if word in self.words: 
                score += math.log(self.word_prob(word, cat))
        return score

    def predict(self, text_input):
        best_cat = None
        test_words = self.split(text_input)
        max_score = -sys.maxsize
        score_list = []
        for cat in self.cat_dict.keys():
            score = self.score(test_words, cat)
            score_list.append((cat, score))
            if score > max_score:
                max_score = score
                best_cat = cat
        return best_cat, score_list

    def get_word_count(self, word, cat):
        if word in self.word_dict[cat]:
            return self.word_dict[cat][word]
        else:
            return 0
    
    def cat_prob(self, cat):
        sum_cat = sum(self.cat_dict.values())
        return self.cat_dict[cat] / sum_cat
    
    def word_prob(self, word, cat):
        n = self.get_word_count(word, cat) + 0.5
        d = sum(self.word_dict[cat].values())
        return n/d 

                