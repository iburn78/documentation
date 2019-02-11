from gensim.models import word2vec
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

fp = codecs.open("2BEXXX01.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("text body")
text = body.getText()

twitter = Twitter()
results = []
lines = text.split("\r\n")
for line in lines:
    malist = twitter.pos(line, norm=True, stem=True)
    r = []
    for word, pumsa in malist:
        if not pumsa in ["Josa", "Eomi", "Punctuation"]:
            r.append(word)
    rl = (" ".join(r)).strip()
    results.append(rl)
    print(rl)
    
wakati_file = 'toji.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))
        
data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1) # size means vector size for a word
model.save("toji.model")

# USING the created model
model = word2vec.Word2Vec.load("toji.model")
print(model.most_similar(positive=["음식"]))  # prints words that are similar to the input

"""
data = wrod2vec.LineSentence("")
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save("")
"""